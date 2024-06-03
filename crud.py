import mysql.connector as mycon
import streamlit as st

mydb = mycon.connect(
    host = "localhost",
    user = "root",
    password ="root",
    database="crud_new1"
)

mycursor = mydb.cursor()
print("Connection Established")

def main():
    st.title("This is my CRUD App")

    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))

    if option == "Create":
        st.header("Create a record")

        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        if st.button("Create"):
            sql = "insert into users(name,email) values(%s,%s)"
            val = (name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!!!")

    elif option == "Read":
        st.header("Read a record")
        mycursor.execute("Select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.header("Update a record")
        id = st.number_input("Enter id")
        name = st.text_input("Enter new Name")
        email = st.text_input("Enter new Email")
        if st.button("update"):
            sql = "update users set name = %s, email = %s where id = %s"
            val = (name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Updated Successfullyy!!!")


    elif option == "Delete":
        st.header("Delete a record")

        id= st.number_input("Enter the id to Delete")
        if st.button("Delete"):
            sql = "delete from users where id = %s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!!")


if __name__ == "__main__":
    main()
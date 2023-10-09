# from fastapi import FastAPI
# import mysql.connector

# app = FastAPI()

# # Function to check the database connection
# def check_db_connection():
#     try:
#         db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root",
#             database="testing"
#         )
#         db.close()  # Close the connection if successful
#         return True
#     except mysql.connector.Error as err:
#         return False

# @app.get("/check-connection")
# async def check_connection():
#     if check_db_connection():
#         return {"message": "Database connection is successful"}
#     else:
#         return {"message": "Unable to connect to the database"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)




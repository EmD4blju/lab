import dotenv
import os

def invoke_lab():
    dotenv.load_dotenv()
    print(os.environ['SOME_KEY'])
    
if __name__ == '__main__':
    invoke_lab()
import random
import string
def generate_password(length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    all_chars=lowercase+uppercase+digits+symbols
    password=random.sample(all_chars, length)
    password_str=''.join(password)
    return password_str
def main():
    length=int(input("Enter the length of the password:"))
    password=generate_password(length)
    print("Generated password:",password)
if __name__=="__main__":
    main()
    

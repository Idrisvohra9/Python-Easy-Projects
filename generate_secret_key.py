import random
import string

def generate_secret_key(length=50):
    """
    Generates a random secret key with the given length.
    
    :param length: The length of the generated secret key.
    :return: A random secret key string.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return secret_key

if __name__ == "__main__":
    # Generate a secret key with the default length of 50 characters
    secret_key = generate_secret_key()
    print("Generated SECRET_KEY:")
    print(secret_key)

import hashlib, os


def get_hash_of_binary_file_contents (file_path, algorithm='MD5'):
  """This function will read and hash the contents of a file. 
  
  :param file_path: The path to the file to be hashed.
  :type file_path: str.
  :param algorithm: The hashing algorithm to be used. Defaults to 'MD5'.
  :type algorithm: str.
  :returns: str -- The hash of the contents of the file.
  """
  file_contents = read_binary_file(file_path)
  file_hash = get_hash_of_string(file_contents, algorithm)
  return file_hash



def get_hash_of_string (string, algorithm='MD5'):
  if algorithm == 'MD5':
    hash_object = hashlib.md5(string)
    hash_digest = hash_object.hexdigest()
  else:
    hash_digest = ''
  return hash_digest


def read_binary_file (file_path):
  try:
    file_object = open(file_path,'rb')
    file_contents = file_object.read()
  except:
    raise
  return file_contents
  
import uuid
import hashlib

hash_object = hashlib.md5(b'harry potter')
print(hash_object.hexdigest())
#this function hashes a new book id.
def hash_book_id(book_id):
	salt = uuid.uuid4().hex
	return hashlib.md5(salt.encode() + book_id.encode()).hexdigest()+':'+salt
#this function verifies the book id.
def book_id_verify(hashed_book_id, reader_account):
	book_id, salt = hashed_book_id.split(':')
	return book_id == hashlib.md5(salt.encode() + reader_account.encode()).hexdigest()
#This will tell you if the book id is correct.
create_new_book_id = 'harry potter'
create_new_book_id = input ('Enter a new book_id: ')
newid = hash_book_id(create_new_book_id)
print('String: ' + newid)
old_book_id = input('Please re-enter book_id: ')
if book_id_verify(newid, old_book_id):
	print('That is the correct book_id')
else:
	print('that is the incorrect book id ')
	
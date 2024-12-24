from minio import Minio
from minio.error import S3Error
from random import random, randint
import os
import time

def main():
   # Create a client with the MinIO server playground, its access key
   # and secret key.
    time.sleep(60)
    client = Minio(
       "localhost:9000",
       access_key="DmTTGIwuIiCUCZldjtVk",
       secret_key="ibgl6at8hs2Ct2ZgPVhiwVfap5WnRvvlXE8DJeeV",
       secure=False,
    )

   # Make 'demo' bucket if not exist.
    found = client.bucket_exists("testminio")
    if not found:
           client.make_bucket("testminio")
    else:
        print("Bucket 'testminio' already exists")

   # Upload 'minio.jpg' as object name
   # 'minio.jpg' to bucket 'demo'.
    fname = "f.txt"
    for i in range(0,1000):
        pref_fname = fname
        fname = str(randint(1,100000000000))+".txt"
        os.rename(pref_fname,fname)
        client.fput_object(
            "testminio",
            fname,
            "./"+fname,
        )
    os.rename(fname,"f.txt")
   #print(
   #    "'im.jpg' is successfully uploaded as "
   #   "object 'im.jpg' to bucket 'test'."
   #)


if __name__ == "__main__":
   try:
       main()
   except S3Error as exc:
       print("error occurred.", exc)

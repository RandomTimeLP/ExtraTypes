from ExtraTypes import snowflake

# Create a snowflake object that auto generates an ID
id1 = snowflake() # create a new snowflake object
print(str(id1)) # print the snowflake object

id2 = snowflake("1234902382727401472") # create a new snowflake object with a given "snowflake ID"
print(str(id2))# printthe snowflake again (if not the creation of the object will raise an exception)

id3 = snowflake(str(id1)) # verifying that the first snowflake object is a valid snowflake ID
print(str(id3)) #


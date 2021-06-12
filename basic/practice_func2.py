# def profile(name,age,main_lang):
#     print("name : {0}\t age : {1}\t main_lang : {2}"\
#         .format(name,age,main_lang))

# profile("yoo",20,"C")
# profile("kim",30,"Java")

#same school, class, age. default value

def profile(name,age=17,main_lang="Python"):
    print("name : {0}\t age : {1}\t main_lang : {2}"\
        .format(name,age,main_lang))

profile("yoo",20,"C")
profile("kim",30,"Java")
profile("Lee")
profile("park")

#keyword call

profile(name="yoo",age=20,main_lang="C")
profile(name="Jeong", main_lang="Perl", age=30)

#가변인자. 호출
# def profile2(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("name : {0}\t age : {1}\t".format(name,age), end=" " )
#     print(lang1,lang2,lang3,lang4,lang5)

def profile2(name,age,*language):
    print("name : {0}\t age : {1}\t".format(name,age), end=" " )
    for lang in language:
        print(lang, end = " ")
    print()    

profile2("Kim",10,"C","Java","C#","Pascal","Fortran","lisp")
profile2("Lee",10,"Kortlin","Swift")
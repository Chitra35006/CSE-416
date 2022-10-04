"""
isJavaScriptFile 
ফাংশন নেম দিতে হবে isJavaScriptFile । এই ফাংশনে প্যারামিটার হিসেবে নিবে একটি স্ট্রিং(String) যেটি হবে একটি ফাইল নেম (যেমনঃ ‘index.js’)। যদি এটি জাভাস্ক্রিপ্ট ফাইল হয় তোমাকে true রিটার্ন করতে হবে আর যদি না হয় তাহলে false রিটার্ন করতে হবে । 

Input            Output
app.js            True
js.png            False
image.js.png      False
image.jpg.js      True

"""


def isJavaScriptFile(fileName):
    errorMessage = "Please Provide a Valid String As Input"
    showMessage = "This is not a JavaScript File"
    if (type(fileName) != str):
        return errorMessage
    elif (type(fileName) == str):
        string1InLower = fileName.casefold()
        subsString = string1InLower[-3:len(string1InLower)]
        if ((subsString.index('.') == len(subsString)-3) and (subsString.index('j') == len(subsString)-2) and (subsString.index('s') == len(subsString)-1)):
            return True
        else:
            return False


value = 'image.js.ks'
result = isJavaScriptFile(value)
print(result)

import requests as session
import re
getRecaptchaToken = session.get("https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LezjdAZAAAAAD1FaW81QpkkplPNzCNnIOU5anHw&co=aHR0cHM6Ly9hY2NvdW50cy5zbmFwY2hhdC5jb206NDQz&hl=en&v=M-QqaF9xk6BpjLH22uHZRhXt&size=invisible&badge=inline&cb=9qlf8d10oqh9")
recaptchaToken = re.findall('recaptcha-token" value="(.+?)"', getRecaptchaToken.text)
if len(recaptchaToken) == 0:
 print(f"Unable to retrieve recaptchaToken.")
else:
 getRecaptchaResponse = session.post("https://www.google.com/recaptcha/enterprise/reload?k=6LezjdAZAAAAAD1FaW81QpkkplPNzCNnIOU5anHw", data={"v": "M-QqaF9xk6BpjLH22uHZRhXt","reason": "q","c": recaptchaToken[0],})
 recaptchaSolution = re.findall('rresp","(.+?)"', getRecaptchaResponse.text)
 print(recaptchaSolution[0])
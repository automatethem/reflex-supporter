# reflex-supporter

https://pypi.org/project/reflex-supporter
<pre>
pip install reflex-supporter
</pre>

Install Node.js (npm) (Windows)  
https://nodejs.org/ko/download/  
https://nodejs.org/download/release/v13.9.0/  

Supported APIs
```
import reflex_supporter

reflex_supporter.components.color_picker
reflex_supporter.components.jumo_button
reflex_supporter.components.json_editor
reflex_supporter.components.webcam
```

app/rxconfig.py  
```
import reflex as rx

class AppConfig(rx.Config):
    pass

#from rxconfig import config
#config.app_name
config = AppConfig(
    app_name="app", #디폴트 app
    #db_url="sqlite:///pynecone.db", #디폴트 sqlite:///pynecone.db
    #api_url="http://localhost:8000", #디폴트 http://localhost:8000 #http://localhost:8000, http://automatethem.net:8000
    #port=3000, #디폴트 3000 #실제 서비스시 추가로 커멘드 라인에서 80 포트를 3000 포트로 포워딩 하기
    #backend_port=8000, #디폴트 8000
    #env=rx.Env.DEV, #디폴트 rx.Env.DEV #rx.Env.DEV, rx.Env.PROD
    #disable_bun=False, #디폴트 False
    frontend_packages=[ 
        #디폴트 없음 #"react-jsondata-editor" 
        "react-colorful", #
        "react-supporter", #
        "react-jsondata-editor" #
        "react-webcam" #
    ]
)
```

Examples:  

https://github.com/automatethem/reflex-supporter/blob/main/examples/color_picker/app/app/app.py  

https://github.com/automatethem/reflex-supporter/blob/main/examples/jumo_button/app/app/app.py  

https://github.com/automatethem/reflex-supporter/blob/main/examples/json_editor/app/app/app.py

<img src="https://github.com/automatethem/reflex-supporter/blob/main/readme_files/screenshot1.PNG?raw=true">

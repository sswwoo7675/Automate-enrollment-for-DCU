from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver = './chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('http://sugang.cu.ac.kr/sugang/')

driver.implicitly_wait(5)

driver.execute_script('''
    function myHookCaptcha(str1, str2) {	
        var canvas = frm.document.getElementById("chapcha");
        if(!!canvas){
            var ctx = frm.document.getElementById("chapcha").getContext("2d");
            ctx.clearRect(0,0,32,20); 
            ctx.beginPath();
            ctx.fillText(str1, 16, 15);
            //frm.document.getElementById("addrndKey").value = str1;
            frm.document.getElementById("cartrndKey").value = str1;
        }
    }
    showCaptchaString = myHookCaptcha;
''')


login_frame = driver.find_element_by_id("ifrm")
driver.switch_to.frame(login_frame)

id = driver.find_element_by_css_selector("#login_id")
id.send_keys("id")

pw = driver.find_element_by_css_selector("#password")
pw.send_keys("pw")

login_btn = driver.find_element_by_css_selector("#btn_login")
login_btn.click()

driver.switch_to.default_content()

in_frame = driver.find_element_by_id("ifrm")
driver.switch_to.frame(in_frame)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartInfo .table_view_tr1")))

driver.execute_script('''
    function my_cart_submit(){

        // key값 입력여부 확인.
        var cartrndKey = document.getElementById("cartrndKey").value;

        if(cartrndKey.length != 2){
            document.getElementById("cartrndKey").focus();
            alert("수강꾸러미 일괄신청 KEY를 입력하세요.");
            return false;
        }

        // 자료 선택여부 확인
        var bCheckYn = false;
        for(var i=0; i < document.getElementById("dummy3").elements.length; i++){
            if(document.getElementById("dummy3").elements[i].type == "checkbox"){
                e = document.getElementById("dummy3").elements[i];
                if(e.checked){
                    bCheckYn = true;
                    continue;
                }
            }
        }

        if(!bCheckYn){
            alert("수강꾸러미 일괄신청 자료를 선택해주세요.");	
            return false;
        }

        actionPro("S");
        cartMsgClear();

        // 수강신청 처리
        var vR = "||";
        var vArr;

        for(var i=0; i < document.getElementById("dummy3").elements.length; i++){
            if(document.getElementById("dummy3").elements[i].type == "checkbox"){
                e = document.getElementById("dummy3").elements[i];
                if(e.checked){
                    vArr = e.value.split(vR);
                    parent.client_mesg('ADD_CLIST' + strTok + vArr[0] + strTok + vArr[1] + strTok + cartrndKey);
                    vSleep(1000);		// 1초 후에 날림.
                }
            }
        }

        // chapchar 변경
        parent.client_mesg("PONG");

        document.getElementById("cartrndKey").value="";
        document.getElementById("addrndKey").value="";
        return false;
    }
    cart_submit = my_cart_submit
''')
driver.execute_script("cart_submit();")
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
                          
        
    



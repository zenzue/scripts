import re
import socket
import requests

raw_email = """
Delivered-To: reciever@gmail.com
Received: by 2002:a05:7022:61a2:b0:68:5041:44f3 with SMTP id n34csp1800063dln;
        Mon, 21 Aug 2023 00:02:54 -0700 (PDT)
X-Google-Smtp-Source: AGHT+IHG9+48iHygclOdqZK/culyXp49oxklJHuYtl2UPOwlK+Qs/BnzCI0YOMSYfOIjJRZSLwOF
X-Received: by 2002:ac8:7f47:0:b0:410:9b45:d7ed with SMTP id g7-20020ac87f47000000b004109b45d7edmr2201151qtk.56.1692601374350;
        Mon, 21 Aug 2023 00:02:54 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1692601374; cv=none;
        d=google.com; s=arc-20160816;
        b=p2+GbLxtw+C7CCMu2O9J3iX0LI+CveEytgi67PfGfU/6ecJiat7iBOtlXCI1RZV6hs
         E+JrCnnCq9ejmSDYrJ2mR5mgDJwQGHutxMfu3IZiT6NFbwxZQKTDZ5NDa+HFkuIUKOfy
         Vtv2TiRxotMI1sPBnPBY5oMYNkxnkMQVWRG9yJ3bMHlnBy16AnF/UzawIKr7eDfkGZMV
         Erdp2VAAuoX9emOLVsG3S6c0KyY20t9d0kiCWKQ2W0iYbDMApPe5+cPsjnIx9L9kYlcF
         H++djlxQt23lNqqtXf5J8UnLyVR4v+nTNw7ztCXMNeAtc8xfZNqJjalNETrkzrdfU5hx
         5C9w==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=mime-version:feedback-id:list-unsubscribe:message-id:subject
         :reply-to:from:to:date;
        bh=5HUmfQLgpEqePHRbpFyiW3xRKD+B/gD5TuTzmTsNp2k=;
        fh=MYPC7G6vxlXgT98kYrLpAow9uPz2W9UVo1pXPrgYBl8=;
        b=EamPdHInLM0PhDINV/a+sqCytY/QZ2d4cz9RmUd2S1Jlw5Vhxltkz8AT229D6Y7oNe
         szUQDRH+jWwZ+4IkjR06krbwc4LTEm3T/J9dXZW0VLXOuQ9/VieIbd2j5eA/7+Nw7dzs
         kOaotHw3C0IItIP9DA2WOQpNTFP2+JLyc8A+zHlIW0ITWkq9JL+/ZyQZVtASmt4Atu28
         RxHqctgS5MxYw+cmHsupsjRa4qfZOuSK2ScyPvOduE0KoNpkv0v8nrx/ShjxAbf0QL8e
         57oIedWRCJzlWlg+viAAAc6UIfdS+/EErq1qxDbkUu2DaMHewaQ/5Ew0kGLzWqLJxipY
         BDyA==
ARC-Authentication-Results: i=1; mx.google.com;
       spf=pass (google.com: domain of campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com designates 162.243.39.218 as permitted sender) smtp.mailfrom="campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com";
       dmarc=fail (p=NONE sp=NONE dis=NONE) header.from=onepay.com.mm
Return-Path: <campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com>
Received: from crmail2.infimail.com (crmail2.infimail.com. [162.243.39.218])
        by mx.google.com with ESMTP id y11-20020a05622a164b00b00403aac185c5si4427690qtj.636.2023.08.21.00.02.53
        for <reciever@gmail.com>;
        Mon, 21 Aug 2023 00:02:54 -0700 (PDT)
Received-SPF: pass (google.com: domain of campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com designates 162.243.39.218 as permitted sender) client-ip=162.243.39.218;
Authentication-Results: mx.google.com;
       spf=pass (google.com: domain of campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com designates 162.243.39.218 as permitted sender) smtp.mailfrom="campaign-onepaycee-180163-36-27566-reciever=gmail.com@ncdelivery.agdbank.com";
       dmarc=fail (p=NONE sp=NONE dis=NONE) header.from=onepay.com.mm
Date: Mon, 21 Aug 2023 12:10:49 +0530
To: reciever@gmail.com
From: Onepay <info@onepay.com.mm>
Reply-To: Onepay <info@onepay.com.mm>
Subject: Pay your electricity bills effortlessly!
Message-ID: <177769702627566@ncdelivery.agdbank.com>
List-Unsubscribe: <mailto:onepaycee-180163-36-27566-734401c2fb2764ebcea99d2b909ba85d@ncdelivery.agdbank.com?subject=Unsubscribe>, <http://panela.onepay.com.mm/vtrack?ul=AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1XVh4=&sl=c014cTQdMzEdYHhsSERTXlcPAh9XClxJAkAXUlhfGFxYTFE=&clientid=180163&c=000>
Feedback-ID: 36:180163:20230821121050:
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="b1_576a2a0848b33128ecac3c6522427d6f"

--b1_576a2a0848b33128ecac3c6522427d6f
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 7bit

 

Onepay နဲ့
မီတာဘေလ်လွယ်ကူစွာပေးဆောင်ပါ။

မီတာရုံးအထိ နေပူခံ
မိုးစိုခံသွားစရာမလိုဘဲ
မီတာဘေလ်ကိုအချိန်မှီပေးဆောင်နိုင်ဖို့
Onepay
အက်ပ်တစ်ခုပဲလိုပါတယ်။

ONE-Bills > Electricity >တွင် ရန်ကုန်၊
မန္တလေး ၊ နေပြည်တော်
ရွေးချယ်ကာ မီတာစာရွက်ပါ
ဘားကုတ်နံပါတ်ကို
ရိုက်ထည့်ပြီး
မီတာဘေလ်ပေးဆောင်နိုင်ပါတယ်။
မီတာဘေလ်ပေးဆောင်ရာတွင်
ကြွေးကျန်များကျန်ရှိနေတာတွေကိုလည်း
တပါတည်းပေါင်းပြီး
ပေးဆောင်နိုင်သလို
ဝန်ဆောင်ခအနေနဲ့လည်း
100ကျပ်သာ
ကျသင့်မှာဖြစ်တာမို့
အပင်ပန်းခံမနေပါနဲ့တော့နော်။

လစဉ်မီတာဘေလ်တွေကို
၁၃ရက်နေ့မှ
စတင်ပေးဆောင်နိုင်မှာ
ဖြစ်ပြီး
မြို့နယ်များအပေါ်မူတည်ပြီးတော့
(၁၇)ရက်မှ (၂၅)ရက်အတွင်း
နောက်ဆုံးထား
ပေးဆောင်ရမှာဖြစ်တာကြောင့်
Onepay နဲ့
မီတာဘေလ်ဆောင်လိုက်တော့နော်။

အက်ပ်တစ်ခုပဲလိုပါတယ်။

အကောင့်အဆင့်မြှင့်တင်နည်းကြည့်ရှုရန်
- http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1TVB4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0DWkEWWE0dX0IVBkNRAkA=&ext=

Make your electricity bill payments hassle-free with Onepay!

Effortlessly pay your electricity bill from the comfort of your home
using ONE-Bills > Electricity with just a few simple clicks. Save time
and simplify your bill payments today with ONE-Bills.

 

How to Verify - http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1TVB4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0DWkEWWE0dX0IVBkNRAkA=&ext=
<http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1TVR4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0UAQEKBAcDBgVNAEUWF1xXB15LWFMcWFRBHw1LHwdcUVoN&ext=dXBuPU14cjRWLTJGLTJGNDQwaTdQcVlhclQzYnl2UTgxLTJGVE1oNld6RnA0QW83MlZLUXlaLTJCRmtKbmh5dk5MZk5oUkpWSWhLWVRjWE5fcS0yQmRwRWNxN1dKZnVDUDQwZnF4c3pOdkJocDBjVUxlelVBMnIzdTJIRWhqMlFpbmw5YUh6WnAyaFNLcTBOT2xxaDNvM3AzV2ZIYXNHM0xPby0yQkdXSTVkRnpvNEJSQmxtbFFpc2xKcjJGQmIwNGwzY1liUUNOT3hrdS0yRlh4ZmR4WVdIRUx6aW43LTJCWXRvMC0yRlpRVFpWeUdiTmxtLTJCaVUxenl0aWM4TnZTT2F6YXVsRDlYR0hNeXlZNnhEdEhXZUdicnMzMEV0SHhLVkYza2M4ek9hdGZ3QmVKcVg5dlZHa0VmTnlnYnhnNDItMkJja0c3cmZydUNqOTRsZ3lqRlNYQ3l2ZWZTQ2hsRExKQm95eC0yRlpKNm1SUzBYMFlSUnZkN1JLLTJGbjA5YWZpV29JbU5NaTFqeXpOZkxIRm1qbkJONkIydVR4TjI0Z0duWW1yMWVROS0yRjREUDJKalR3OHV3WWFwTmF0MVVyYU1lMGc4LTJCZzJWYmFHcWNYNlEzeWhUWlRNMThsWUFwM3hBVlNaemIxVU9INktxcHpmVE1Ba3dKazktMkZRdVpjTHJzYWFUZ1hwRnJmRVV5Ti0yQkNaRFhnZXAxSmg1UFl1Z1gtMkZnU3N0aGwtMkZuLTJGWUJpQU11cUlTZ1laaHJ2Rk1lVkdGWDFMMEZ0Z1Nmd2ItMkI2Wk5HM1ZYZTJXdmFvWDQtMkZHNlVJUEJGR2pVUDd0RlNBbGJBRmtZOEgxcUs2cWpLQzRORmVsNndja05QdVFwMEd6cXJuRS0yQmZrcjlNQ00xQTRsclc1TmVaY2dGVml5NFhmVzNJVUstMkZUYjZUcW0tMkZCbW9ZdGplWlU2M05tcjJqWFg4N3pmYjdpM2RGN21NV1UtMkJidHZ6TVRHaDRkYWZLazNJSHdveE56amJybXREcHE2d1lGTGMtMkJ1REZjQVJoYlV3bkxQSS0yQkRLMExiNkJSa0U2eEFIYXZ2RnBILTJGRDY5NXo4RFY3bTlzWlpUci0yRnpYQU92S0V2OTc5WlpDSkJSNXZFdnJUSC0yQlp3MTdZVm9CWi0yQk9JLTJGOUN4ZmhqMDR6RFNqU04yRm1yNDltaldvVmlQY1d2WG9OUEhjSDkxWXhmbWptMmJFaDU0NlU2Z09TcUxxWHphLTJGRXZmbEF0MnVoRTdBbHlMNGtrZXRLSG5aSjloWHh1cVNtZ2tUZ0xscHNOVzV2RnFNei0yQlk4ZXdvSEsxLTJGNG9wTW1FVHhmOGNKWXU2Mjloc2JOMDFKSHhJOFV6UzZGakVIZXBTS2ZZcVFNa3l4by0yRkdwelhET2s1U2VYYUZMa2tCdGVGbDZ3b2NIVzZrVlh6MUxIMlExYUdYdVd1ZzA3SFVaSzNoN3FkOGhGYTJGaDVRTEVxVS0zRA==>

Pay Bills Now <http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1WGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQltOSQ0PVllRWl8cRF1MDF9dFFhADlQ=&ext=>

 

 <http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1ZGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWUlVRVVAMDFoWB1ZUTFZXVEdTT1xY&ext=>

 <http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1YGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0IXUZMVVNAUV9NAF5VS1ZXBklYSFpf&ext=>
 <http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1QVh4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWWF1cW1cHCl8WB1ZUTFpWXEdTWEgaXw9dQAVJVVQ=&ext=>
 <http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1QVx4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWQF1ZRF0ITVJXCRZ5DFdcQVZLW0hUXgxZQg==&ext=>

--Click Here to unsubscribe from this newsletter.


--b1_576a2a0848b33128ecac3c6522427d6f
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 8bit

<!DOCTYPE html><html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en"><head><title></title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><style>
*{box-sizing:border-box}body{margin:0;padding:0}a[x-apple-data-detectors]{color:inherit!important;text-decoration:inherit!important}#MessageViewBody a{color:inherit;text-decoration:none}p{line-height:inherit}.desktop_hide,.desktop_hide table{mso-hide:all;display:none;max-height:0;overflow:hidden}.image_block img+div{display:none} @media (max-width:520px){.social_block.desktop_hide .social-table{display:inline-block!important}.mobile_hide{display:none}.row-content{width:100%!important}.stack
 .column{width:100%;display:block}.mobile_hide{min-height:0;max-height:0;max-width:0;overflow:hidden;font-size:0}.desktop_hide,.desktop_hide table{display:table!important;max-height:none!important}}
</style></head><body style="background-color:#fff;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none"><table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;background-color:#fff"><tbody><tr><td><table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tbody><tr><td><table 
class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;color:#000;width:500px;margin:0 auto" width="500"><tbody><tr><td class="column column-1" width="100%" style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;padding-bottom:5px;padding-top:5px;vertical-align:top;border-top:0;border-right:0;border-bottom:0;border-left:0"><table class="image_block block-1" width="100%" border="0" 
cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad" style="width:100%"><div class="alignment" align="center" style="line-height:10px"><img src="https://d1l8l3rp33cdzs.cloudfront.net/images/onepaycee/editor_images/User%20Header.png" style="display:block;height:auto;border:0;max-width:500px;width:100%" width="500"></div></td></tr></table><table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" 
role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad" style="width:100%"><div class="alignment" align="center" style="line-height:10px"><img src="https://d1l8l3rp33cdzs.cloudfront.net/images/onepaycee/EDM%20EPC.png" style="display:block;height:auto;border:0;max-width:500px;width:100%" width="500"></div></td></tr></table><table class="divider_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" 
style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="divider_inner" style="font-size:1px;line-height:1px;border-top:1px solid #bbb"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="text_block block-4" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" 
style="mso-table-lspace:0;mso-table-rspace:0;word-break:break-word"><tr><td class="pad"><div style="font-family:sans-serif"><div class style="font-size:12px; 
font-family:Arial,'Helvetica Neue',Helvetica,sans-serif;mso-line-height-alt:14.399999999999999px;color:#555;line-height:1.2"><p style="margin:0;font-size:12px;mso-line-height-alt:14.399999999999999px"><strong>Onepay &#4116;&#4146;&#4151; &#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4124;&#4157;&#4122;&#4154;&#4096;&#4144;&#4101;&#4157;&#4140;&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4117;&#4139;&#4171;</strong><br><br>
&#4121;&#4142;&#4112;&#4140;&#4123;&#4143;&#4150;&#4152;&#4129;&#4113;&#4141; &#4116;&#4145;&#4117;&#4144;&#4097;&#4150; &#4121;&#4141;&#4143;&#4152;&#4101;&#4141;&#4143;&#4097;&#4150;&#4126;&#4157;&#4140;&#4152;&#4101;&#4123;&#4140;&#4121;&#4124;&#4141;&#4143;&#4120;&#4146; &#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4096;&#4141;&#4143;&#4129;&#4097;&#4155;&#4141;&#4116;&#4154;&#4121;&#4158;&#4142;&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4116;&#4141;&#4143;&#4100;&#4154;&#4118;&#4141;&#4143;&#4151; Onepay
&#4129;&#4096;&#4154;&#4117;&#4154;&#4112;&#4101;&#4154;&#4097;&#4143;&#4117;&#4146;&#4124;&#4141;&#4143;&#4117;&#4139;&#4112;&#4122;&#4154;&#4171;<br><br>ONE-Bills &gt; Electricity &gt;&#4112;&#4157;&#4100;&#4154; &#4123;&#4116;&#4154;&#4096;&#4143;&#4116;&#4154;&#4170; &#4121;&#4116;&#4153;&#4112;&#4124;&#4145;&#4152; &#4170; &#4116;&#4145;&#4117;&#4156;&#4106;&#4154;&#4112;&#4145;&#4140;&#4154; &#4123;&#4157;&#4145;&#4152;&#4097;&#4155;&#4122;&#4154;&#4096;&#4140; &#4121;&#4142;&#4112;&#4140;&#4101;&#4140;&#4123;&#4157;&#4096;&#4154;&#4117;&#4139;
&#4120;&#4140;&#4152;&#4096;&#4143;&#4112;&#4154;&#4116;&#4150;&#4117;&#4139;&#4112;&#4154;&#4096;&#4141;&#4143; &#4123;&#4141;&#4143;&#4096;&#4154;&#4113;&#4106;&#4151;&#4154;&#4117;&#4156;&#4142;&#4152; &#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4116;&#4141;&#4143;&#4100;&#4154;&#4117;&#4139;&#4112;&#4122;&#4154;&#4171; &#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4123;&#4140;&#4112;&#4157;&#4100;&#4154;
&#4096;&#4156;&#4157;&#4145;&#4152;&#4096;&#4155;&#4116;&#4154;&#4121;&#4155;&#4140;&#4152;&#4096;&#4155;&#4116;&#4154;&#4123;&#4158;&#4141;&#4116;&#4145;&#4112;&#4140;&#4112;&#4157;&#4145;&#4096;&#4141;&#4143;&#4124;&#4106;&#4154;&#4152; &#4112;&#4117;&#4139;&#4112;&#4106;&#4154;&#4152;&#4117;&#4145;&#4139;&#4100;&#4154;&#4152;&#4117;&#4156;&#4142;&#4152; &#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4116;&#4141;&#4143;&#4100;&#4154;&#4126;&#4124;&#4141;&#4143;
&#4125;&#4116;&#4154;&#4102;&#4145;&#4140;&#4100;&#4154;&#4097;&#4129;&#4116;&#4145;&#4116;&#4146;&#4151;&#4124;&#4106;&#4154;&#4152; 100&#4096;&#4155;&#4117;&#4154;&#4126;&#4140; &#4096;&#4155;&#4126;&#4100;&#4151;&#4154;&#4121;&#4158;&#4140;&#4118;&#4156;&#4101;&#4154;&#4112;&#4140;&#4121;&#4141;&#4143;&#4151; &#4129;&#4117;&#4100;&#4154;&#4117;&#4116;&#4154;&#4152;&#4097;&#4150;&#4121;&#4116;&#4145;&#4117;&#4139;&#4116;&#4146;&#4151;&#4112;&#4145;&#4140;&#4151;&#4116;&#4145;&#4140;&#4154;&#4171;<br><br>
&#4124;&#4101;&#4105;&#4154;&#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4112;&#4157;&#4145;&#4096;&#4141;&#4143; &#4161;&#4163;&#4123;&#4096;&#4154;&#4116;&#4145;&#4151;&#4121;&#4158; &#4101;&#4112;&#4100;&#4154;&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4116;&#4141;&#4143;&#4100;&#4154;&#4121;&#4158;&#4140; &#4118;&#4156;&#4101;&#4154;&#4117;&#4156;&#4142;&#4152;
&#4121;&#4156;&#4141;&#4143;&#4151;&#4116;&#4122;&#4154;&#4121;&#4155;&#4140;&#4152;&#4129;&#4117;&#4145;&#4139;&#4154;&#4121;&#4144;&#4112;&#4106;&#4154;&#4117;&#4156;&#4142;&#4152;&#4112;&#4145;&#4140;&#4151; (&#4161;&#4167;)&#4123;&#4096;&#4154;&#4121;&#4158; (&#4162;&#4165;)&#4123;&#4096;&#4154;&#4129;&#4112;&#4157;&#4100;&#4154;&#4152; &#4116;&#4145;&#4140;&#4096;&#4154;&#4102;&#4143;&#4150;&#4152;&#4113;&#4140;&#4152;
&#4117;&#4145;&#4152;&#4102;&#4145;&#4140;&#4100;&#4154;&#4123;&#4121;&#4158;&#4140;&#4118;&#4156;&#4101;&#4154;&#4112;&#4140;&#4096;&#4156;&#4145;&#4140;&#4100;&#4151;&#4154; Onepay &#4116;&#4146;&#4151;
&#4121;&#4142;&#4112;&#4140;&#4120;&#4145;&#4124;&#4154;&#4102;&#4145;&#4140;&#4100;&#4154;&#4124;&#4141;&#4143;&#4096;&#4154;&#4112;&#4145;&#4140;&#4151;&#4116;&#4145;&#4140;&#4154;&#4171;<br><br>&#4129;&#4096;&#4154;&#4117;&#4154;&#4112;&#4101;&#4154;&#4097;&#4143;&#4117;&#4146;&#4124;&#4141;&#4143;&#4117;&#4139;&#4112;&#4122;&#4154;&#4171;<br><br>&#4129;&#4096;&#4145;&#4140;&#4100;&#4151;&#4154;&#4129;&#4102;&#4100;&#4151;&#4154;&#4121;&#4156;&#4158;&#4100;&#4151;&#4154;&#4112;&#4100;&#4154;&#4116;&#4106;&#4154;&#4152;&#4096;&#4156;&#4106;&#4151;&#4154;&#4123;&#4158;&#4143;&#4123;&#4116;&#4154;
- <a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1TVB4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0DWkEWWE0dX0IVBkNRAkA=&ext="  target="_blank" style="text-decoration: underline; color: #0068A5;" rel="noopener">https://bit.ly/opverify</a><br><br><br><br></p><p 
style="margin:0;mso-line-height-alt:14.399999999999999px"><strong>Make your electricity bill payments hassle-free with Onepay!</strong><br><br>Effortlessly pay your electricity bill from the comfort of your home using ONE-Bills &gt; Electricity with just a few simple clicks. Save time and simplify your bill payments today with ONE-Bills.</p><p style="margin:0;mso-line-height-alt:14.399999999999999px">&nbsp;</p><p style="margin:0;mso-line-height-alt:14.399999999999999px">
How to Verify - <a
href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1TVR4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0UAQEKBAcDBgVNAEUWF1xXB15LWFMcWFRBHw1LHwdcUVoN&ext=dXBuPU14cjRWLTJGLTJGNDQwaTdQcVlhclQzYnl2UTgxLTJGVE1oNld6RnA0QW83MlZLUXlaLTJCRmtKbmh5dk5MZk5oUkpWSWhLWVRjWE5fcS0yQmRwRWNxN1dKZnVDUDQwZnF4c3pOdkJocDBjVUxlelVBMnIzdTJIRWhqMlFpbmw5YUh6WnAyaFNLcTBOT2xxaDNvM3AzV2ZIYXNHM0xPby0yQkdXSTVkRnpvNEJSQmxtbFFpc2xKcjJGQmIwNGwzY1liUUNOT3hrdS0yRlh4ZmR4WVdIRUx6aW43LTJCWXRvMC0yRlpRVFpWeUdiTmxtLTJCaVUxenl0aWM4TnZTT2F6YXVsRDlYR0hNeXlZNnhEdEhXZUdicnMzMEV0SHhLVkYza2M4ek9hdGZ3QmVKcVg5dlZHa0VmTnlnYnhnNDItMkJja0c3cmZydUNqOTRsZ3lqRlNYQ3l2ZWZTQ2hsRExKQm95eC0yRlpKNm1SUzBYMFlSUnZkN1JLLTJGbjA5YWZpV29JbU5NaTFqeXpOZkxIRm1qbkJONkIydVR4TjI0Z0duWW1yMWVROS0yRjREUDJKalR3OHV3WWFwTmF0MVVyYU1lMGc4LTJCZzJWYmFHcWNYNlEzeWhUWlRNMThsWUFwM3hBVlNaemIxVU9INktxcHpmVE1Ba3dKazktMkZRdVpjTHJzYWFUZ1hwRnJmRVV5Ti0yQkNaRFhnZXAxSmg1UFl1Z1gtMkZnU3N0aGwtMkZuLTJGWUJpQU11cUlTZ1laaHJ2Rk1lVkdGWDFMMEZ0Z1Nmd2ItMkI2Wk5HM1ZYZTJXdmFvWDQtMkZHNlVJUEJGR2pVUDd0RlNBbGJBRmtZOEgxcUs2cWpLQzRORmVsNndja05QdVFwMEd6cXJuRS0yQmZrcjlNQ00xQTRsclc1TmVaY2dGVml5NFhmVzNJVUstMkZUYjZUcW0tMkZCbW9ZdGplWlU2M05tcjJqWFg4N3pmYjdpM2RGN21NV1UtMkJidHZ6TVRHaDRkYWZLazNJSHdveE56amJybXREcHE2d1lGTGMtMkJ1REZjQVJoYlV3bkxQSS0yQkRLMExiNkJSa0U2eEFIYXZ2RnBILTJGRDY5NXo4RFY3bTlzWlpUci0yRnpYQU92S0V2OTc5WlpDSkJSNXZFdnJUSC0yQlp3MTdZVm9CWi0yQk9JLTJGOUN4ZmhqMDR6RFNqU04yRm1yNDltaldvVmlQY1d2WG9OUEhjSDkxWXhmbWptMmJFaDU0NlU2Z09TcUxxWHphLTJGRXZmbEF0MnVoRTdBbHlMNGtrZXRLSG5aSjloWHh1cVNtZ2tUZ0xscHNOVzV2RnFNei0yQlk4ZXdvSEsxLTJGNG9wTW1FVHhmOGNKWXU2Mjloc2JOMDFKSHhJOFV6UzZGakVIZXBTS2ZZcVFNa3l4by0yRkdwelhET2s1U2VYYUZMa2tCdGVGbDZ3b2NIVzZrVlh6MUxIMlExYUdYdVd1ZzA3SFVaSzNoN3FkOGhGYTJGaDVRTEVxVS0zRA=="

target="_blank" style="text-decoration: underline; color: #0068A5;" rel="noopener">https://bit.ly/opverify</a></p></div></div></td></tr></table><table class="button_block block-5" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad"><div class="alignment" align="center">
<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://onelink.to/onepaymm" style="height:38px;width:131px;v-text-anchor:middle;" arcsize="93%" stroke="false" fillcolor="#00a78c"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; 
font-family:Arial, sans-serif; font-size:14px"><![endif]-->
<a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1WGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQltOSQ0PVllRWl8cRF1MDF9dFFhADlQ=&ext="  target="_blank" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#00a78c;border-radius:35px;width:auto;border-top:0px solid transparent;font-weight:700;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px; 
font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:14px;text-align:center;mso-border-alt:none;word-break:keep-all;"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 28px;">Pay Bills Now</span></span></a>
<!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div></td></tr></table><table class="divider_block block-6" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad"><div class="alignment" align="center"><table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="divider_inner" 
style="font-size:1px;line-height:1px;border-top:1px solid #bbb"><span>&#8202;</span></td></tr></table></div></td></tr></table><table class="social_block block-7" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0"><tr><td class="pad"><div class="alignment" align="center"><table class="social-table" width="144px" border="0" cellpadding="0" cellspacing="0" role="presentation" 
style="mso-table-lspace:0;mso-table-rspace:0;display:inline-block"><tr><td style="padding:0 2px 0 2px"><a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1ZGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWUlVRVVAMDFoWB1ZUTFZXVEdTT1xY&ext="  target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/facebook@2x.png" width="32" height="32" alt="Facebook" title="Facebook" style="display:block;height:auto;border:0"></a></td><td style="padding:0 2px 0 2px">
<a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1YGg==&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0IXUZMVVNAUV9NAF5VS1ZXBklYSFpf&ext="  target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/instagram@2x.png" width="32" height="32" alt="Instagram" title="Instagram" style="display:block;height:auto;border:0"></a></td><td style="padding:0 2px 0 2px"><a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1QVh4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWWF1cW1cHCl8WB1ZUTFpWXEdTWEgaXw9dQAVJVVQ=&ext="  target="_blank"><img 
src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/linkedin@2x.png" width="32" height="32" alt="LinkedIn" title="LinkedIn" style="display:block;height:auto;border:0"></a></td><td style="padding:0 2px 0 2px"><a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1QVx4=&sl=c010TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQhJbSU0WREIWQF1ZRF0ITVJXCRZ5DFdcQVZLW0hUXgxZQg==&ext="  target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/circle-color/tiktok@2x.png" width="32" height="32" alt="TikTok" title="TikTok" 
style="display:block;height:auto;border:0"></a></td></tr></table></div></td></tr></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><!-- End --><br/><div><p style='font-size: 12px;line-height: normal;font-family: arial;text-align: center;' >--<br><a href="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1UXx4=&sl=c01iTjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&pp=0&fl=WUVDQltOSRIAXVBUVRpdXlcTAkgWB1ZUTVRUHlhcU0FUSQJdVUs=&ext=cD1zbXVuc3ViJm1pZD0zNiZ1aWQ9W1VOSVFJRF0="  >Click Here</a> to unsubscribe from this newsletter.<br><br></div><img border="0" src="http://panela.onepay.com.mm/vtrack?clientid=180163&ul=
AwYCBFcdVx4bVltCQVEDAwFUI1ZVBVBVTVpWXEtO&ml=AgdLAh1RGg==&sl=c014TjQyGjEsZ0lIVVpXXFNNDF9dFFhATVpWXBlfW00F&c=180163" ></body></html>



--b1_576a2a0848b33128ecac3c6522427d6f--
"""

def decode_mime_header(header):
    try:
        parts = header.split("=?")
        charset = parts[1]
        encoding = parts[2]
        encoded_text = parts[3]
        decoded_text = encoded_text.decode(encoding)
        return decoded_text.encode('latin-1').decode(charset)
    except Exception as e:
        return header

header_lines = raw_email.split('\n')

headers = {}

for line in header_lines:    
    match = re.match(r'([^:]+): (.+)', line)
    if match:
        field_name, field_value = match.groups()
        headers[field_name] = decode_mime_header(field_value)

def get_ip_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "IP information not available"}
    except Exception as e:
        return {"error": str(e)}

print("From:", headers.get("From", "N/A"))
print("To:", headers.get("To", "N/A"))
print("Subject:", headers.get("Subject", "N/A"))
print("Date:", headers.get("Date", "N/A"))

received_headers = headers.get("Received", "")
ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', received_headers)

for ip_address in reversed(ip_addresses):
    if ip_address != "127.0.0.1" and ip_address != "localhost":
        sender_ip = ip_address
        break

if sender_ip:
    print("Sender's IP Address:", sender_ip)

    ip_info = get_ip_info(sender_ip)
    if "error" not in ip_info:
        print("IP Information:")
        print(f"  IP Address: {ip_info['ip']}")
        print(f"  Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"  City: {ip_info.get('city', 'N/A')}")
        print(f"  Region: {ip_info.get('region', 'N/A')}")
        print(f"  Country: {ip_info.get('country', 'N/A')}")
    else:
        print("IP Information: N/A")

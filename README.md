# Anten 
<a href="https://ibb.co/W2YbsD1"><img src="https://i.ibb.co/0GdgQB3/a.png" alt="a" border="0" style="center" /></a>
# توضیحات
آموزش رایگان ساخت پروفایل برای ایفون های سری 14 و 15.
این برنامه به زبان پایتون نوشته شده و شما توسط این برنامه میتونید بخش های اولیه و مهم کانفیگ پروفایل رو به صورت اختصاصی شخصی سازی کنید.

# قبل از استفاده :
1. ابتدا ریست نتورک را انجام دهید 🔄.
2. فایل کانفیگ ساخته شده با هر روشی به گوشی ارسال کنید و آن را دانلود کنید و سپس بر روی آن کلیک کنید تا باز شود، سپس آن را در فایل ذخیره کنید 💾.
3. سپس به فایل منیجر بروید و روی کانفیگ کلیک کنید تا یک پیام بالا بیاید و اماده نصب شود 📂.
4. سپس وارد تنظیمات بخش VPN و Device Management شوید، پروفایل را انتخاب کرده و نصب کنید 📲.
5. بعد از نصب، به بخش Cellular Data بروید، تیک Data Roaming و VoLTE را بر روی 5G یا LTE بزنید، سپس گوشی را روشن و خاموش کنید تا آنتن برگردد 📶.

حالا بر روی [لینک شورتکات](https://www.icloud.com/shortcuts/9b2f6b908fb74058b2b1bf3ed4d08451) کلیک کنید 📌:
6. از توی شورتکات روی Anten کلیک کرده و نصبش کنید 📱.

و اگه انتن قطع شد با فعال کردن Shortcut میتونید مجدد راه اندازی کنید 🔄.

تمام شما آنتن دارید 📶.

# چند نکته مهم:

1. روی شبکه همراه اول تنظیم کنید تا آنتن بهتر بازگردد 📡.
2. از دو سیم کارت همزمان در گوشی استفاده نکنید 🚫.
3. در صورت کار نکردن پروفایل با uuid جدید بسازید و تست کنید همچنین برای دسترسی اینترنت مخصوصا برای ایرانسل میتونید تنظیمات ip رو ip6 بذارید 🌐.
4. حتماً نت را روی 5G تنظیم کنید 📶.
5. اگر از ساعت ۱۲ شب آنتن ندارید، نت را روی 2G تنظیم کنید، زیرا در برخی موارد آنتن به طور اتوماتیک تا صبح ۸ برگردد 🌙.

همچنین به یاد داشته باشید که هر پروفایل جدیدی که می‌خواهید تست کنید، قبل از آن باید پروفایل قبلی را پاک کنید ❌.

# نحوه استفاده :
شما باید پایتون نسخه 3 رو روی سیستمون نصب کنید.
[آموزش نصب پایتون 3](https://www.youtube.com/watch?v=k7XXsTWgIMU)

**دریافت فایل :**
1. (Linux/MacOs) Terminal Base :
    * `git clone https://github.com/IR0DayToday/Anten`

2. (Windows) CMD Base :
    * فایل رو ازاین [قسمت دانلود](https://github.com/IR0DayToday/Anten/archive/refs/heads/main.zip) کنید.
    * فایل دریافتی را از حالت فشرده خارج کنید
    * فایل anten.py رو با دستور `python anten.py` اجرا کنید.

## بخش های قابل تغییر
1. Payload UUID 
    * در این قسمت شما میتوانید UUID اختصاصی خودتون رو وارد کنید در صورت وارد نکردن برنامه به صورت خودکار بهتون یک UUID اختصاصی میسازه.
---
2. Payload Identifier:
    * در این قسمت شما میتونید Payload Identifier اختصاصی خودتون رو وارد کنید در صورت عدم وارد کردن برنامه به صورت اتوماتیک از روی UUID برای شما یک Payload Identifier اختصاصی تعیین میکنه.
        * Payload Identifier چیست :
        ---
            توضیح "Payload Identifier" در فایل‌های تنظیمات (Configuration Profiles)
            Payload Identifier یک شناسه یکتا (unique identifier) است که در فایل‌های تنظیمات (configuration profiles) به هر بخش از تنظیمات (payload) اختصاص داده می‌شود. فایل‌های تنظیمات معمولاً با فرمت .mobileconfig ذخیره می‌شوند و شامل تنظیمات مختلفی هستند که توسط مدیران سیستم یا کاربران حرفه‌ای برای پیکربندی دستگاه‌های iOS و macOS ایجاد می‌شوند. هر بخش از تنظیمات می‌تواند شامل پیکربندی‌هایی مانند Wi-Fi، ایمیل، VPN، تنظیمات دستگاه و غیره باشد.
            شناسه یکتای "Payload Identifier" به این دلیل اهمیت دارد که:
            تمایز بخش‌های مختلف تنظیمات: هر بخش از تنظیمات در یک فایل تنظیمات باید دارای شناسه‌ای یکتا باشد تا سیستم بتواند آنها را از هم تمیز دهد.
            مدیریت بهتر تنظیمات: با استفاده از این شناسه، مدیران سیستم می‌توانند به سادگی تنظیمات خاصی را شناسایی و در صورت نیاز تغییر یا به‌روزرسانی کنند.
            پیشگیری از تداخل تنظیمات: با داشتن شناسه‌های یکتا، از تداخل و تکرار ناخواسته تنظیمات مشابه در یک فایل جلوگیری می‌شود.
            نمونه فایل تنظیمات (Configuration Profile) با استفاده از "Payload Identifier"
            در این مثال، یک فایل تنظیمات شامل دو بخش پیکربندی Wi-Fi و ایمیل ایجاد می‌کنیم. هر بخش دارای یک "Payload Identifier" یکتا است که به مدیریت و شناسایی آن کمک می‌کند.
            یک مثال :
            ``<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
            <plist version="1.0">
            <dict>
                <key>PayloadContent</key>
                <array>
                    <!-- پیکربندی Wi-Fi -->
                    <dict>
                        <key>PayloadType</key>
                        <string>com.apple.wifi.managed</string>
                        <key>PayloadVersion</key>
                        <integer>1</integer>
                        <key>PayloadIdentifier</key>
                        <string>com.example.configuration.wifi</string>
                        <key>PayloadUUID</key>
                        <string>12345678-1234-1234-1234-1234567890AB</string>
                        <key>PayloadDisplayName</key>
                        <string>Wi-Fi Configuration</string>
                        <key>SSID_STR</key>
                        <string>ExampleWiFi</string>
                        <key>HIDDEN_NETWORK</key>
                        <false/>
                        <key>AutoJoin</key>
                        <true/>
                        <key>EncryptionType</key>
                        <string>WPA</string>
                        <key>Password</key>
                        <string>examplepassword</string>
                    </dict>

                    <!-- پیکربندی ایمیل -->
                    <dict>
                        <key>PayloadType</key>
                        <string>com.apple.mail.managed</string>
                        <key>PayloadVersion</key>
                        <integer>1</integer>
                        <key>PayloadIdentifier</key>
                        <string>com.example.configuration.email</string>
                        <key>PayloadUUID</key>
                        <string>87654321-4321-4321-4321-0987654321BA</string>
                        <key>PayloadDisplayName</key>
                        <string>Email Configuration</string>
                        <key>EmailAccountDescription</key>
                        <string>Example Email</string>
                        <key>EmailAccountType</key>
                        <string>EmailTypeIMAP</string>
                        <key>EmailAddress</key>
                        <string>user@example.com</string>
                        <key>IncomingMailServerHostName</key>
                        <string>imap.example.com</string>
                        <key>IncomingMailServerPortNumber</key>
                        <integer>993</integer>
                        <key>IncomingMailServerUseSSL</key>
                        <true/>
                        <key>IncomingMailServerUsername</key>
                        <string>user@example.com</string>
                        <key>IncomingMailServerPassword</key>
                        <string>emailpassword</string>
                        <key>OutgoingMailServerHostName</key>
                        <string>smtp.example.com</string>
                        <key>OutgoingMailServerPortNumber</key>
                        <integer>587</integer>
                        <key>OutgoingMailServerUseSSL</key>
                        <true/>
                        <key>OutgoingMailServerUsername</key>
                        <string>user@example.com</string>
                        <key>OutgoingMailServerPassword</key>
                        <string>emailpassword</string>
                    </dict>
                </array>
                <key>PayloadType</key>
                <string>Configuration</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
                <key>PayloadIdentifier</key>
                <string>com.example.configuration</string>
                <key>PayloadUUID</key>
                <string>ABCDEFAB-ABCD-ABCD-ABCD-ABCDEFABCDEF</string>
                <key>PayloadDisplayName</key>
                <string>Example Configuration Profile</string>
            </dict>
            </plist>
            ``
            ساختار فایل: این فایل با استفاده از فرمت XML و استاندارد plist ایجاد شده است.
            PayloadContent: این کلید شامل یک آرایه از دیکشنری‌ها است که هر دیکشنری نمایانگر یک بخش از تنظیمات (payload) است.
            PayloadType: نوع تنظیمات را مشخص می‌کند (مثلاً com.apple.wifi.managed برای Wi-Fi و com.apple.mail.managed برای ایمیل).
            PayloadVersion: نسخه تنظیمات را مشخص می‌کند. در اینجا نسخه 1 است.
            PayloadIdentifier: شناسه یکتایی است که هر بخش از تنظیمات را مشخص می‌کند (مثلاً com.example.configuration.wifi برای Wi-Fi و com.example.configuration.email برای ایمیل).
            PayloadUUID: یک شناسه یکتا برای هر بخش از تنظیمات است که به صورت خودکار تولید می‌شود.
            PayloadDisplayName: نام نمایشی برای هر بخش از تنظیمات است که در رابط کاربری نمایش داده می‌شود.

3. Proxy Server:
    * برای اینکه بتوانید پراکسی اختصاصی خودتون رو وارد کنید. اگر در این قسمت چیزی وارد نکنید بخش پراکسی در کانفیگتون خالی خواهد ماند.
---
4. Proxy Port:
    * پورت مربوط به پراکسی سرور در این قسمت وارد میشود. در صورت خالی گذاشتن در کانفیگ هم اعمال نخواهد شد.
---
5. Authentication Type:
    * PAP : Password Authentication Protocol
        * این پروتکل ساده است و رمز عبور را به صورت متنی (plain text) ارسال می‌کند و کمترین میزان امنیت را دارد ولی سازگاری بیشتری با شبکه‌های مختلف دارد.
    * CHAP : Challenge Handshake Authentication Protocol
        * از یک روش چالشی استفاده می‌کند که امنیت بیشتری نسبت به PAP دارد و رمز عبور به صورت متنی ارسال نمی‌شود و از یک مکانیسم چالشی-پاسخی (Handshake) استفاده می‌کند.
    * MS-CHAP : Microsoft Challenge Handshake Authentication Protocol
        * این نوع از CHAP برای سیستم‌های ویندوز توسعه یافته است و از آن برای احراز هویت در شبکه‌های مایکروسافتی استفاده می‌شود.


    * EAP : Extensible Authentication Protocol
        * یک پروتکل احراز هویت قابل توسعه است که از آن برای احراز هویت در اتصالات شبکه بی‌سیم و VPN استفاده می‌شود. این پروتکل قابلیت پشتیبانی از روش‌های احراز هویت مختلف را فراهم می‌کند، از جمله EAP-TLS (EAP with Transport Layer Security)، EAP-TTLS (EAP Tunneled Transport Layer Security)، و PEAP (Protected Extensible Authentication Protocol).
    
    * OAuth : Open Authorization
        * یک پروتکل احراز هویت و اجازه‌دهی برای دسترسی به منابع شبکه است که عمدتا برای اتصال به سرویس‌های وب و شبکه‌های اجتماعی استفاده می‌شود.
    
    * RADIUS : Remote Authentication Dial-In User Service
        * یک پروتکل شبکه است که برای احراز هویت و مدیریت دسترسی کاربران به شبکه استفاده می‌شود. این پروتکل از CHAP و PAP نیز پشتیبانی می‌کند.
    
    * LDAP : Lightweight Directory Access Protocol
        * یک پروتکل مبتنی بر شبکه است که برای دسترسی به سرویس‌های دایرکتوری مورد استفاده قرار می‌گیرد، از جمله اطلاعات احراز هویت.
    
    ⚠️ **در این قسمت شما بهتره از پروتکل های PAP و CHAP استفاده کنید.**
---
6. APPName :
    * IRANCELL (ایرانسل) : 
        * mtnirancell
        * SYSTEC
    * MCI (همراه اول):
        * mcinet
        * cmcom
    * RighTel (رایتل):
        *Rightel


# نسخه وب این اسکریپ :
[WEB-Script-Base](https://aigptcode.github.io/iphoneprofile/)

# راه های ارتباطی و خبرنامه ها :
1. **Telegram** :
    * CHANNEL 01 :  [Click](https://t.me/LearnExploit)
    * CHANNEL 02 : [Click](https://t.me/BypassNetwork)
    * GROUP : [Click](https://t.me/LearnExploit_Group)

2. **Twitter** : [Click](https://x.com/aigptcode)

# تنظیمات دستی
اگر شما تمایل دارید همه ی این پروسه رو به صورت دستی انجام بدید به گیتهاب زیر مراجعه کنید:
**GITHUB** : [AIGPTCODE](https://github.com/AiGptCode/Iphone-14-15-IRAN-Anten)




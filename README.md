# Neko-ConfigGrabber

<p align="center">
  <b>Eat Telegram Xray Configs Like a Neko</b>
</p></br>

<p align="center">This is a Python script that collects VPN Configs from various Channels and groups and saves them to a Json file for other scripts.</p>

<p align="center"><strong>🔴 <em>We recommend using a secondary account or an account that you don't frequently use.</em> 🔴</strong></p></br>

# امکانات

   • ✅ سرعت بسیار بالا در جمع آوری کانفیگ ها 

   • ✅ قابلیت جمع کردن کانفیگ ها از Code Block های پست های تلگرام

   • ✅ دریافت انواع کانفیگ های xray از کانال ها و گروه ها

   • ✅ پشتیبانی از کانال ها و گروه های شخصی

   • ✅ خروجی به صورت json و Machine-readable

## How to use
1. Fork this repository and make sure the repository is **private**.
2. Obtain your Telegram API ID and hash from my.telegram.org
   
**windows and linux :**
   
  3. Download [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) From Official Websites.
  
  4. Clone your private repository to your device.
  
  5. Edit lines 10-11 of `Grabber.py` with your Telegram API ID and hash.
     
  6. Edit line 12 of `Grabber.py` with your config file URL (you can see `source.conf.example` for the config file structure).
     
  7. Run `Grabber.py` on your PC and complete the initial setup (enter your mobile number and OTP code).
     
     ```
     pip install telethon requests
     python Grabber.py
     ```
     
  8. Commit the new files to your repository and enable read and write permissions for GitHub Actions in the repository settings.

     ```
     git add -A && git commit -m "config file edited" && git push
     ```

**android (termux) :**

  3. install Git and Python.

     ```
     apt update
     apt upgrade
     pkg install git
     pkg install python
     ```
     
  4. Clone your private repository to your device.

     ```
     git clone https://github.com/YOURUSERNAME/Neko-ConfigGrabber.git
     cd Neko-ConfigGrabber
     ```
     
  5. Edit lines 10-11 of `Grabber.py` with your Telegram API ID and hash.
  6. Edit line 12 of `Grabber.py` with your config file URL (you can see `source.conf.example` for the config file structure). **(Optional)**
  7. Run `Grabber.py` on your PC and complete the initial setup (enter your mobile number and OTP code).

     ```
     pip install telethon requests
     python Grabber.py
     ```

  8. Commit the new files to your repository and enable read and write permissions for GitHub Actions in the repository settings.
      
      ```
      git add -A && git commit -m "config file edited" && git push
      ```




**Done.**

Now you will get the configs in the configs.json file Every 3 Hours.

## Config File structure

   The configuration file should follow the structure below:

   ```
   channel_username1,channel_username2,channel_username3,private_channel_id1,private_channel_id2,private_group_id1,private_group_id2
   ```

   1. **No Spaces in Usernames**

      Usernames should not contain any spaces. Ensure there are no spaces before, after, or within the usernames.

   2. **Manual Joining For Private Chats**

      You must manually join the private channels and groups before including their names in the configuration file.

   3. **Full id for Private Channels and Groups**

      Use the full id of private channels or groups.

## TODO 🔧
1. Add JSON configs support.
2. Normal Subscription Output

## Disclaimer

Please note that after running `Grabber.py`, the repository will contain personal configuration files. Ensure that your repository remains private to protect your sensitive information. **Do not share or distribute your repository.**

No Warranty: This project is provided "as is" without any warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The entire risk as to the quality and performance of the project is with you.

No Liability: In no event shall the authors be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the project or the use or other dealings in the project.

## License

This project is licensed under the GPL-3.0 license. See the LICENSE file for details.

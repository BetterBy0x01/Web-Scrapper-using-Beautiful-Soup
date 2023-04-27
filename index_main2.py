from bs4 import BeautifulSoup
import json

html_code = """
<li class="module-title open"><a class="module"
        href="https://pen300.hide01.ir/media/video/CSCEO_00_00.mp4"
        data-media-path="media/video/CSCEO_00_00.mp4" data-caption-path="media/captions/CSCEO_00_00.vtt">Client Side Code Execution With Office </a>
        <ul class="submenu">
        <li><a class="sub-module active"
                href="https://pen300.hide01.ir/media/video/CSCEO_01_00.mp4"
                data-media-path="media/video/CSCEO_01_00.mp4"
                data-caption-path="media/captions/CSCEO_01_00.vtt">Will You Be My Dropper</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_01_01.mp4"
                        data-media-path="media/video/CSCEO_01_01.mp4"
                        data-caption-path="media/captions/CSCEO_01_01.vtt">Staged vs Non-staged Payloads</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_01_02.mp4"
                        data-media-path="media/video/CSCEO_01_02.mp4"
                        data-caption-path="media/captions/CSCEO_01_02.vtt">Building Our Droppers</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_01_03.mp4"
                        data-media-path="media/video/CSCEO_01_03.mp4"
                        data-caption-path="media/captions/CSCEO_01_03.vtt">HTML Smuggling</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_02_00.mp4"
                data-media-path="media/video/CSCEO_02_00.mp4"
                data-caption-path="media/captions/CSCEO_02_00.vtt">Phishing with Microsoft Office</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_02_01.mp4"
                        data-media-path="media/video/CSCEO_02_01.mp4"
                        data-caption-path="media/captions/CSCEO_02_01.vtt">Introduction to VBA</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_02_02.mp4"
                        data-media-path="media/video/CSCEO_02_02.mp4"
                        data-caption-path="media/captions/CSCEO_02_02.vtt">Let PowerShell Help Us</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_03_00.mp4"
                data-media-path="media/video/CSCEO_03_00.mp4"
                data-caption-path="media/captions/CSCEO_03_00.vtt">Keeping Up Appearances</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_03_01.mp4"
                        data-media-path="media/video/CSCEO_03_01.mp4"
                        data-caption-path="media/captions/CSCEO_03_01.vtt">Phishing PreTexting</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_03_02.mp4"
                        data-media-path="media/video/CSCEO_03_02.mp4"
                        data-caption-path="media/captions/CSCEO_03_02.vtt">The Old Switcheroo</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_04_00.mp4"
                data-media-path="media/video/CSCEO_04_00.mp4"
                data-caption-path="media/captions/CSCEO_04_00.vtt">Executing Shellcode in Word Memory</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_04_01.mp4"
                        data-media-path="media/video/CSCEO_04_01.mp4"
                        data-caption-path="media/captions/CSCEO_04_01.vtt">Calling Win32 APIs from VBA</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_04_02.mp4"
                        data-media-path="media/video/CSCEO_04_02.mp4"
                        data-caption-path="media/captions/CSCEO_04_02.vtt">VBA Shellcode Runner</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_05_00.mp4"
                data-media-path="media/video/CSCEO_05_00.mp4"
                data-caption-path="media/captions/CSCEO_05_00.vtt">PowerShell Shellcode Runner</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_05_01.mp4"
                        data-media-path="media/video/CSCEO_05_01.mp4"
                        data-caption-path="media/captions/CSCEO_05_01.vtt">Calling Win32 APIs from PowerShell</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_05_02.mp4"
                        data-media-path="media/video/CSCEO_05_02.mp4"
                        data-caption-path="media/captions/CSCEO_05_02.vtt">Porting Shellcode Runner to PowerShell</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_06_00.mp4"
                data-media-path="media/video/CSCEO_06_00.mp4"
                data-caption-path="media/captions/CSCEO_06_00.vtt">Keep That PowerShell in Memory</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_06_01.mp4"
                        data-media-path="media/video/CSCEO_06_01.mp4"
                        data-caption-path="media/captions/CSCEO_06_01.vtt">Add-Type Compilation</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_06_02.mp4"
                        data-media-path="media/video/CSCEO_06_02.mp4"
                        data-caption-path="media/captions/CSCEO_06_02.vtt">Leveraging UnsafeNativeMethods</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_06_03.mp4"
                        data-media-path="media/video/CSCEO_06_03.mp4"
                        data-caption-path="media/captions/CSCEO_06_03.vtt">DelegateType Reflection</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_06_04.mp4"
                        data-media-path="media/video/CSCEO_06_04.mp4"
                        data-caption-path="media/captions/CSCEO_06_04.vtt">Reflection Shellcode Runner in PowerShell</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_07_00.mp4"
                data-media-path="media/video/CSCEO_07_00.mp4"
                data-caption-path="media/captions/CSCEO_07_00.vtt">Talking To The Proxy</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_07_01.mp4"
                        data-media-path="media/video/CSCEO_07_01.mp4"
                        data-caption-path="media/captions/CSCEO_07_01.vtt">PowerShell Proxy-Aware Communication</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_07_02.mp4"
                        data-media-path="media/video/CSCEO_07_02.mp4"
                        data-caption-path="media/captions/CSCEO_07_02.vtt">Fiddling With The User-Agent</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEO_07_03.mp4"
                        data-media-path="media/video/CSCEO_07_03.mp4"
                        data-caption-path="media/captions/CSCEO_07_03.vtt">Give Me A SYSTEM Proxy</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEO_08_00.mp4"
                data-media-path="media/video/CSCEO_08_00.mp4"
                data-caption-path="media/captions/CSCEO_08_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/CSCEJ_00_00.mp4"
        data-media-path="media/video/CSCEJ_00_00.mp4" data-caption-path="media/captions/CSCEJ_00_00.vtt">Client Side Code Execution With Windows Script Host</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEJ_01_00.mp4"
                data-media-path="media/video/CSCEJ_01_00.mp4"
                data-caption-path="media/captions/CSCEJ_01_00.vtt">Creating a Basic Dropper in Jscript</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_01_01.mp4"
                        data-media-path="media/video/CSCEJ_01_01.mp4"
                        data-caption-path="media/captions/CSCEJ_01_01.vtt">Execution of Jscript on Windows</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_01_02.mp4"
                        data-media-path="media/video/CSCEJ_01_02.mp4"
                        data-caption-path="media/captions/CSCEJ_01_02.vtt">Jscript Meterpreter Dropper</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEJ_02_00.mp4"
                data-media-path="media/video/CSCEJ_02_00.mp4"
                data-caption-path="media/captions/CSCEJ_02_00.vtt">Jscript and C#</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_01.mp4"
                        data-media-path="media/video/CSCEJ_02_01.mp4"
                        data-caption-path="media/captions/CSCEJ_02_01.vtt">Introduction to Visual Studio</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_02.mp4"
                        data-media-path="media/video/CSCEJ_02_02.mp4"
                        data-caption-path="media/captions/CSCEJ_02_02.vtt">DotNetToJscript</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_03.mp4"
                        data-media-path="media/video/CSCEJ_02_03.mp4"
                        data-caption-path="media/captions/CSCEJ_02_03.vtt">Win32 API Calls From C#</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_04.mp4"
                        data-media-path="media/video/CSCEJ_02_04.mp4"
                        data-caption-path="media/captions/CSCEJ_02_04.vtt">Shellcode Runner in C#</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_05.mp4"
                        data-media-path="media/video/CSCEJ_02_05.mp4"
                        data-caption-path="media/captions/CSCEJ_02_05.vtt">Jscript Shellcode Runner</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_02_06.mp4"
                        data-media-path="media/video/CSCEJ_02_06.mp4"
                        data-caption-path="media/captions/CSCEJ_02_06.vtt">SharpShooter</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEJ_03_00.mp4"
                data-media-path="media/video/CSCEJ_03_00.mp4"
                data-caption-path="media/captions/CSCEJ_03_00.vtt">In-memory PowerShell Revisited</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CSCEJ_03_01.mp4"
                        data-media-path="media/video/CSCEJ_03_01.mp4"
                        data-caption-path="media/captions/CSCEJ_03_01.vtt">Reflective Load</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CSCEJ_04_00.mp4"
                data-media-path="media/video/CSCEJ_04_00.mp4"
                data-caption-path="media/captions/CSCEJ_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/PIM_00_00.mp4"
        data-media-path="media/video/PIM_00_00.mp4" data-caption-path="media/captions/PIM_00_00.vtt">Process Injection and Migration</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/PIM_01_00.mp4"
                data-media-path="media/video/PIM_01_00.mp4"
                data-caption-path="media/captions/PIM_01_00.vtt">Finding a Home for Our Shellcode</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_01_01.mp4"
                        data-media-path="media/video/PIM_01_01.mp4"
                        data-caption-path="media/captions/PIM_01_01.vtt">Process Injection and Migration Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_01_02.mp4"
                        data-media-path="media/video/PIM_01_02.mp4"
                        data-caption-path="media/captions/PIM_01_02.vtt">Process Injection in C#</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/PIM_02_00.mp4"
                data-media-path="media/video/PIM_02_00.mp4" data-caption-path="media/captions/PIM_02_00.vtt">DLL Injection</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_02_01.mp4"
                        data-media-path="media/video/PIM_02_01.mp4"
                        data-caption-path="media/captions/PIM_02_01.vtt">DLL Injection Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_02_02.mp4"
                        data-media-path="media/video/PIM_02_02.mp4"
                        data-caption-path="media/captions/PIM_02_02.vtt">DLL Injection with C#</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/PIM_03_00.mp4"
                data-media-path="media/video/PIM_03_00.mp4"
                data-caption-path="media/captions/PIM_03_00.vtt">Reflective DLL Injection</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_03_01.mp4"
                        data-media-path="media/video/PIM_03_01.mp4"
                        data-caption-path="media/captions/PIM_03_01.vtt">Reflective DLL Injection Theory</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_03_02.mp4"
                        data-media-path="media/video/PIM_03_02.mp4"
                        data-caption-path="media/captions/PIM_03_02.vtt">Reflective DLL Injection in PowerShell</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/PIM_04_00.mp4"
                data-media-path="media/video/PIM_04_00.mp4"
                data-caption-path="media/captions/PIM_04_00.vtt">Process Hollowing</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_04_01.mp4"
                        data-media-path="media/video/PIM_04_01.mp4"
                        data-caption-path="media/captions/PIM_04_01.vtt">Process Hollowing Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/PIM_04_02.mp4"
                        data-media-path="media/video/PIM_04_02.mp4"
                        data-caption-path="media/captions/PIM_04_02.vtt">Process Hollowing in C#</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/PIM_05_00.mp4"
                data-media-path="media/video/PIM_05_00.mp4"
                data-caption-path="media/captions/PIM_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/AVINTRO_00_00.mp4"
        data-media-path="media/video/AVINTRO_00_00.mp4"
        data-caption-path="media/captions/AVINTRO_00_00.vtt">Introduction to Antivirus Evasion</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_01_00.mp4"
                data-media-path="media/video/AVINTRO_01_00.mp4"
                data-caption-path="media/captions/AVINTRO_01_00.vtt">Antivirus Software Overview</a></li>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_02_00.mp4"
                data-media-path="media/video/AVINTRO_02_00.mp4"
                data-caption-path="media/captions/AVINTRO_02_00.vtt">Simulating the Target Environment</a></li>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_03_00.mp4"
                data-media-path="media/video/AVINTRO_03_00.mp4"
                data-caption-path="media/captions/AVINTRO_03_00.vtt">Locating Signatures in Files</a></li>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_04_00.mp4"
                data-media-path="media/video/AVINTRO_04_00.mp4"
                data-caption-path="media/captions/AVINTRO_04_00.vtt">Bypassing Antivirus with Metasploit</a>
        </li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_04_01.mp4"
                        data-media-path="media/video/AVINTRO_04_01.mp4"
                        data-caption-path="media/captions/AVINTRO_04_01.vtt">Metasploit Encoders</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_04_02.mp4"
                        data-media-path="media/video/AVINTRO_04_02.mp4"
                        data-caption-path="media/captions/AVINTRO_04_02.vtt">Metasploit Encryptors</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_05_00.mp4"
                data-media-path="media/video/AVINTRO_05_00.mp4"
                data-caption-path="media/captions/AVINTRO_05_00.vtt">Bypassing Antivirus with C#</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_05_01.mp4"
                        data-media-path="media/video/AVINTRO_05_01.mp4"
                        data-caption-path="media/captions/AVINTRO_05_01.vtt">C# Shellcode Runner vs Antivirus</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_05_02.mp4"
                        data-media-path="media/video/AVINTRO_05_02.mp4"
                        data-caption-path="media/captions/AVINTRO_05_02.vtt">Encrypting the C# Shellcode Runner</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_06_00.mp4"
                data-media-path="media/video/AVINTRO_06_00.mp4"
                data-caption-path="media/captions/AVINTRO_06_00.vtt">Messing with Our Behavior</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_06_01.mp4"
                        data-media-path="media/video/AVINTRO_06_01.mp4"
                        data-caption-path="media/captions/AVINTRO_06_01.vtt">Simple Sleep Timers</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_06_02.mp4"
                        data-media-path="media/video/AVINTRO_06_02.mp4"
                        data-caption-path="media/captions/AVINTRO_06_02.vtt">Non-emulated APIs</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_07_00.mp4"
                data-media-path="media/video/AVINTRO_07_00.mp4"
                data-caption-path="media/captions/AVINTRO_07_00.vtt">Office Please Bypass Antivirus</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_07_01.mp4"
                        data-media-path="media/video/AVINTRO_07_01.mp4"
                        data-caption-path="media/captions/AVINTRO_07_01.vtt">Bypassing Antivirus in VBA</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_07_02.mp4"
                        data-media-path="media/video/AVINTRO_07_02.mp4"
                        data-caption-path="media/captions/AVINTRO_07_02.vtt">Stomping On Microsoft Word</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_08_00.mp4"
                data-media-path="media/video/AVINTRO_08_00.mp4"
                data-caption-path="media/captions/AVINTRO_08_00.vtt">Hiding PowerShell Inside VBA</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_08_01.mp4"
                        data-media-path="media/video/AVINTRO_08_01.mp4"
                        data-caption-path="media/captions/AVINTRO_08_01.vtt">Detection of PowerShell Shellcode Runner</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_08_02.mp4"
                        data-media-path="media/video/AVINTRO_08_02.mp4"
                        data-caption-path="media/captions/AVINTRO_08_02.vtt">Dechaining with WMI</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVINTRO_08_03.mp4"
                        data-media-path="media/video/AVINTRO_08_03.mp4"
                        data-caption-path="media/captions/AVINTRO_08_03.vtt">Obfuscating VBA</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVINTRO_09_00.mp4"
                data-media-path="media/video/AVINTRO_09_00.mp4"
                data-caption-path="media/captions/AVINTRO_09_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/AVADV_00_00.mp4"
        data-media-path="media/video/AVADV_00_00.mp4"
        data-caption-path="media/captions/AVADV_00_00.vtt">Advanced Antivirus Evasion</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_01_00.mp4"
                data-media-path="media/video/AVADV_01_00.mp4"
                data-caption-path="media/captions/AVADV_01_00.vtt">Intel Architecture and Windows 10</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_01_01.mp4"
                        data-media-path="media/video/AVADV_01_01.mp4"
                        data-caption-path="media/captions/AVADV_01_01.vtt">WinDbg Introduction</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_02_00.mp4"
                data-media-path="media/video/AVADV_02_00.mp4"
                data-caption-path="media/captions/AVADV_02_00.vtt">Antimalware Scan Interface</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_02_01.mp4"
                        data-media-path="media/video/AVADV_02_01.mp4"
                        data-caption-path="media/captions/AVADV_02_01.vtt">Understanding AMSI</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_02_02.mp4"
                        data-media-path="media/video/AVADV_02_02.mp4"
                        data-caption-path="media/captions/AVADV_02_02.vtt">Hooking with Frida</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_03_00.mp4"
                data-media-path="media/video/AVADV_03_00.mp4"
                data-caption-path="media/captions/AVADV_03_00.vtt">Bypassing AMSI With Reflection in PowerShell</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_03_01.mp4"
                        data-media-path="media/video/AVADV_03_01.mp4"
                        data-caption-path="media/captions/AVADV_03_01.vtt">What Context Mom?</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_03_02.mp4"
                        data-media-path="media/video/AVADV_03_02.mp4"
                        data-caption-path="media/captions/AVADV_03_02.vtt">Attacking Initialization</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_04_00.mp4"
                data-media-path="media/video/AVADV_04_00.mp4"
                data-caption-path="media/captions/AVADV_04_00.vtt">Wrecking AMSI in PowerShell</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_04_01.mp4"
                        data-media-path="media/video/AVADV_04_01.mp4"
                        data-caption-path="media/captions/AVADV_04_01.vtt">Understanding the Assembly Flow</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_04_02.mp4"
                        data-media-path="media/video/AVADV_04_02.mp4"
                        data-caption-path="media/captions/AVADV_04_02.vtt">Patching the Internals</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_05_00.mp4"
                data-media-path="media/video/AVADV_05_00.mp4"
                data-caption-path="media/captions/AVADV_05_00.vtt">UAC Bypass vs Microsoft Defender</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_05_01.mp4"
                        data-media-path="media/video/AVADV_05_01.mp4"
                        data-caption-path="media/captions/AVADV_05_01.vtt">FodHelper UAC Bypass</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_05_02.mp4"
                        data-media-path="media/video/AVADV_05_02.mp4"
                        data-caption-path="media/captions/AVADV_05_02.vtt">Improving Fodhelper</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_06_00.mp4"
                data-media-path="media/video/AVADV_06_00.mp4"
                data-caption-path="media/captions/AVADV_06_00.vtt">Bypassing AMSI in Jscript</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_06_01.mp4"
                        data-media-path="media/video/AVADV_06_01.mp4"
                        data-caption-path="media/captions/AVADV_06_01.vtt">Detecting the AMSI API Flow</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_06_02.mp4"
                        data-media-path="media/video/AVADV_06_02.mp4"
                        data-caption-path="media/captions/AVADV_06_02.vtt">Is That Your Registry Key?</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AVADV_06_03.mp4"
                        data-media-path="media/video/AVADV_06_03.mp4"
                        data-caption-path="media/captions/AVADV_06_03.vtt">I Am My Own Executable</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AVADV_07_00.mp4"
                data-media-path="media/video/AVADV_07_00.mp4"
                data-caption-path="media/captions/AVADV_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/AW_00_00.mp4"
        data-media-path="media/video/AW_00_00.mp4" data-caption-path="media/captions/AW_00_00.vtt">Application Whitelisting</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_01_00.mp4"
                data-media-path="media/video/AW_01_00.mp4"
                data-caption-path="media/captions/AW_01_00.vtt">Application Whitelisting Theory and Setup</a>
        </li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_01_01.mp4"
                        data-media-path="media/video/AW_01_01.mp4"
                        data-caption-path="media/captions/AW_01_01.vtt">Application Whitelisting Theory</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_01_02.mp4"
                        data-media-path="media/video/AW_01_02.mp4"
                        data-caption-path="media/captions/AW_01_02.vtt">AppLocker Setup and Rules</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_02_00.mp4"
                data-media-path="media/video/AW_02_00.mp4" data-caption-path="media/captions/AW_02_00.vtt">Basic Bypasses</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_02_01.mp4"
                        data-media-path="media/video/AW_02_01.mp4"
                        data-caption-path="media/captions/AW_02_01.vtt">Trusted Folders</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_02_02.mp4"
                        data-media-path="media/video/AW_02_02.mp4"
                        data-caption-path="media/captions/AW_02_02.vtt">Bypass With DLLs</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_02_03.mp4"
                        data-media-path="media/video/AW_02_03.mp4"
                        data-caption-path="media/captions/AW_02_03.vtt">Alternate Data Streams</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_02_04.mp4"
                        data-media-path="media/video/AW_02_04.mp4"
                        data-caption-path="media/captions/AW_02_04.vtt">Third Party Execution</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_03_00.mp4"
                data-media-path="media/video/AW_03_00.mp4"
                data-caption-path="media/captions/AW_03_00.vtt">Bypassing AppLocker with PowerShell</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_03_01.mp4"
                        data-media-path="media/video/AW_03_01.mp4"
                        data-caption-path="media/captions/AW_03_01.vtt">PowerShell Constrained Language Mode</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_03_02.mp4"
                        data-media-path="media/video/AW_03_02.mp4"
                        data-caption-path="media/captions/AW_03_02.vtt">Custom Runspaces</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_03_03.mp4"
                        data-media-path="media/video/AW_03_03.mp4"
                        data-caption-path="media/captions/AW_03_03.vtt">PowerShell CLM Bypass</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_03_04.mp4"
                        data-media-path="media/video/AW_03_04.mp4"
                        data-caption-path="media/captions/AW_03_04.vtt">Reflective Injection Returns</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_04_00.mp4"
                data-media-path="media/video/AW_04_00.mp4"
                data-caption-path="media/captions/AW_04_00.vtt">Bypassing AppLocker with C#</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_04_01.mp4"
                        data-media-path="media/video/AW_04_01.mp4"
                        data-caption-path="media/captions/AW_04_01.vtt">Locating a Target</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_04_02.mp4"
                        data-media-path="media/video/AW_04_02.mp4"
                        data-caption-path="media/captions/AW_04_02.vtt">Reverse Engineering for Load</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_04_03.mp4"
                        data-media-path="media/video/AW_04_03.mp4"
                        data-caption-path="media/captions/AW_04_03.vtt">Give Me Code Exec</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_04_04.mp4"
                        data-media-path="media/video/AW_04_04.mp4"
                        data-caption-path="media/captions/AW_04_04.vtt">Invoking the Target Part 1</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_04_05.mp4"
                        data-media-path="media/video/AW_04_05.mp4"
                        data-caption-path="media/captions/AW_04_05.vtt">Invoking the Target Part 2</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_05_00.mp4"
                data-media-path="media/video/AW_05_00.mp4"
                data-caption-path="media/captions/AW_05_00.vtt">Bypassing AppLocker with JScript</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_05_01.mp4"
                        data-media-path="media/video/AW_05_01.mp4"
                        data-caption-path="media/captions/AW_05_01.vtt">JScript and MSHTA</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AW_05_02.mp4"
                        data-media-path="media/video/AW_05_02.mp4"
                        data-caption-path="media/captions/AW_05_02.vtt">XSL Transform</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AW_06_00.mp4"
                data-media-path="media/video/AW_06_00.mp4"
                data-caption-path="media/captions/AW_06_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/IDS_00_00.mp4"
        data-media-path="media/video/IDS_00_00.mp4" data-caption-path="media/captions/IDS_00_00.vtt">Bypassing Network Filters</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_01_00.mp4"
                data-media-path="media/video/IDS_01_00.mp4" data-caption-path="media/captions/IDS_01_00.vtt">DNS Filters</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_01_01.mp4"
                        data-media-path="media/video/IDS_01_01.mp4"
                        data-caption-path="media/captions/IDS_01_01.vtt">Dealing with DNS Filters</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_02_00.mp4"
                data-media-path="media/video/IDS_02_00.mp4" data-caption-path="media/captions/IDS_02_00.vtt">Web Proxies</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_02_01.mp4"
                        data-media-path="media/video/IDS_02_01.mp4"
                        data-caption-path="media/captions/IDS_02_01.vtt">Bypassing Web Proxies</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_03_00.mp4"
                data-media-path="media/video/IDS_03_00.mp4" data-caption-path="media/captions/IDS_03_00.vtt">IDS and IPS Sensors</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_03_01.mp4"
                        data-media-path="media/video/IDS_03_01.mp4"
                        data-caption-path="media/captions/IDS_03_01.vtt">Case study: Bypassing Norton HIPS with Custom Certificates</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_04_00.mp4"
                data-media-path="media/video/IDS_04_00.mp4"
                data-caption-path="media/captions/IDS_04_00.vtt">Full Packet Capture Devices</a></li>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_05_00.mp4"
                data-media-path="media/video/IDS_05_00.mp4"
                data-caption-path="media/captions/IDS_05_00.vtt">HTTPS Inspection</a></li>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_06_00.mp4"
                data-media-path="media/video/IDS_06_00.mp4"
                data-caption-path="media/captions/IDS_06_00.vtt">Domain Fronting</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_06_01.mp4"
                        data-media-path="media/video/IDS_06_01.mp4"
                        data-caption-path="media/captions/IDS_06_01.vtt">Domain Fronting in The Lab</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_07_00.mp4"
                data-media-path="media/video/IDS_07_00.mp4" data-caption-path="media/captions/IDS_07_00.vtt">DNS Tunneling</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_07_01.mp4"
                        data-media-path="media/video/IDS_07_01.mp4"
                        data-caption-path="media/captions/IDS_07_01.vtt">How DNS Tunneling Works</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/IDS_07_02.mp4"
                        data-media-path="media/video/IDS_07_02.mp4"
                        data-caption-path="media/captions/IDS_07_02.vtt">DNS Tunneling with dnscat2</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/IDS_08_00.mp4"
                data-media-path="media/video/IDS_08_00.mp4"
                data-caption-path="media/captions/IDS_08_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/LPE_00_00.mp4"
        data-media-path="media/video/LPE_00_00.mp4" data-caption-path="media/captions/LPE_00_00.vtt">Linux Post-Exploitation</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LPE_01_00.mp4"
                data-media-path="media/video/LPE_01_00.mp4"
                data-caption-path="media/captions/LPE_01_00.vtt">User Configuration Files</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_01_01.mp4"
                        data-media-path="media/video/LPE_01_01.mp4"
                        data-caption-path="media/captions/LPE_01_01.vtt">VIM Config Simple Backdoor</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_01_02.mp4"
                        data-media-path="media/video/LPE_01_02.mp4"
                        data-caption-path="media/captions/LPE_01_02.vtt">VIM Config Simple Keylogger</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LPE_02_00.mp4"
                data-media-path="media/video/LPE_02_00.mp4"
                data-caption-path="media/captions/LPE_02_00.vtt">Bypassing AV</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_02_01.mp4"
                        data-media-path="media/video/LPE_02_01.mp4"
                        data-caption-path="media/captions/LPE_02_01.vtt">Kaspersky Endpoint Security</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_02_02.mp4"
                        data-media-path="media/video/LPE_02_02.mp4"
                        data-caption-path="media/captions/LPE_02_02.vtt">Antiscan.me</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LPE_03_00.mp4"
                data-media-path="media/video/LPE_03_00.mp4"
                data-caption-path="media/captions/LPE_03_00.vtt">Shared Libraries</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_03_01.mp4"
                        data-media-path="media/video/LPE_03_01.mp4"
                        data-caption-path="media/captions/LPE_03_01.vtt">How Shared Libraries Work on Linux</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_03_02.mp4"
                        data-media-path="media/video/LPE_03_02.mp4"
                        data-caption-path="media/captions/LPE_03_02.vtt">Shared Library Hijacking via LD_LIBRARY_PATH</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LPE_03_03.mp4"
                        data-media-path="media/video/LPE_03_03.mp4"
                        data-caption-path="media/captions/LPE_03_03.vtt">Exploitation via LD_PRELOAD</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LPE_04_00.mp4"
                data-media-path="media/video/LPE_04_00.mp4"
                data-caption-path="media/captions/LPE_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/KIOSK_00_00.mp4"
        data-media-path="media/video/KIOSK_00_00.mp4" data-caption-path="media/captions/KIOSK_00_00.vtt">Kiosk Breakouts</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/KIOSK_01_00.mp4"
                data-media-path="media/video/KIOSK_01_00.mp4"
                data-caption-path="media/captions/KIOSK_01_00.vtt">Kiosk Enumeration</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_01_01.mp4"
                        data-media-path="media/video/KIOSK_01_01.mp4"
                        data-caption-path="media/captions/KIOSK_01_01.vtt">Kiosk Browser Enumeration</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/KIOSK_02_00.mp4"
                data-media-path="media/video/KIOSK_02_00.mp4"
                data-caption-path="media/captions/KIOSK_02_00.vtt">Command Execution</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_02_01.mp4"
                        data-media-path="media/video/KIOSK_02_01.mp4"
                        data-caption-path="media/captions/KIOSK_02_01.vtt">Exploring the Filesystem</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_02_02.mp4"
                        data-media-path="media/video/KIOSK_02_02.mp4"
                        data-caption-path="media/captions/KIOSK_02_02.vtt">Leveraging Firefox Profiles</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_02_03.mp4"
                        data-media-path="media/video/KIOSK_02_03.mp4"
                        data-caption-path="media/captions/KIOSK_02_03.vtt">Enumerating System Information</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_02_04.mp4"
                        data-media-path="media/video/KIOSK_02_04.mp4"
                        data-caption-path="media/captions/KIOSK_02_04.vtt">Scratching the Surface</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/KIOSK_03_00.mp4"
                data-media-path="media/video/KIOSK_03_00.mp4"
                data-caption-path="media/captions/KIOSK_03_00.vtt">Post-Exploitation</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_03_01.mp4"
                        data-media-path="media/video/KIOSK_03_01.mp4"
                        data-caption-path="media/captions/KIOSK_03_01.vtt">Simulating an Interactive Shell</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/KIOSK_04_00.mp4"
                data-media-path="media/video/KIOSK_04_00.mp4"
                data-caption-path="media/captions/KIOSK_04_00.vtt">Privilege Escalation</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_04_01.mp4"
                        data-media-path="media/video/KIOSK_04_01.mp4"
                        data-caption-path="media/captions/KIOSK_04_01.vtt">Thinking Outside the Box</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_04_02.mp4"
                        data-media-path="media/video/KIOSK_04_02.mp4"
                        data-caption-path="media/captions/KIOSK_04_02.vtt">Root Shell at the Top of the Hour</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/KIOSK_04_03.mp4"
                        data-media-path="media/video/KIOSK_04_03.mp4"
                        data-caption-path="media/captions/KIOSK_04_03.vtt">Getting Root Terminal Access</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/KIOSK_05_00.mp4"
                data-media-path="media/video/KIOSK_05_00.mp4"
                data-caption-path="media/captions/KIOSK_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/WC_00_00.mp4"
        data-media-path="media/video/WC_00_00.mp4" data-caption-path="media/captions/WC_00_00.vtt">Windows Credentials</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/WC_01_00.mp4"
                data-media-path="media/video/WC_01_00.mp4" data-caption-path="media/captions/WC_01_00.vtt">Local Windows Credentials</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_01_01.mp4"
                        data-media-path="media/video/WC_01_01.mp4"
                        data-caption-path="media/captions/WC_01_01.vtt">SAM Database</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_01_02.mp4"
                        data-media-path="media/video/WC_01_02.mp4"
                        data-caption-path="media/captions/WC_01_02.vtt">Hardening the Local Administrator Account</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/WC_02_00.mp4"
                data-media-path="media/video/WC_02_00.mp4"
                data-caption-path="media/captions/WC_02_00.vtt">Access Tokens</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_02_01.mp4"
                        data-media-path="media/video/WC_02_01.mp4"
                        data-caption-path="media/captions/WC_02_01.vtt">Access Token Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_02_02.mp4"
                        data-media-path="media/video/WC_02_02.mp4"
                        data-caption-path="media/captions/WC_02_02.vtt">Elevation with Impersonation</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_02_03.mp4"
                        data-media-path="media/video/WC_02_03.mp4"
                        data-caption-path="media/captions/WC_02_03.vtt">Fun with Incognito</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/WC_03_00.mp4"
                data-media-path="media/video/WC_03_00.mp4"
                data-caption-path="media/captions/WC_03_00.vtt">Kerberos and Domain Credentials</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_03_01.mp4"
                        data-media-path="media/video/WC_03_01.mp4"
                        data-caption-path="media/captions/WC_03_01.vtt">Kerberos Authentication</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_03_02.mp4"
                        data-media-path="media/video/WC_03_02.mp4"
                        data-caption-path="media/captions/WC_03_02.vtt">Mimikatz</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/WC_04_00.mp4"
                data-media-path="media/video/WC_04_00.mp4"
                data-caption-path="media/captions/WC_04_00.vtt">Processing Credentials Offline</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_04_01.mp4"
                        data-media-path="media/video/WC_04_01.mp4"
                        data-caption-path="media/captions/WC_04_01.vtt">Memory Dump</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/WC_04_02.mp4"
                        data-media-path="media/video/WC_04_02.mp4"
                        data-caption-path="media/captions/WC_04_02.vtt">MiniDumpWriteDump</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/WC_05_00.mp4"
                data-media-path="media/video/WC_05_00.mp4"
                data-caption-path="media/captions/WC_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/LM_00_00.mp4"
        data-media-path="media/video/LM_00_00.mp4" data-caption-path="media/captions/LM_00_00.vtt">Windows Lateral Movement</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LM_01_00.mp4"
                data-media-path="media/video/LM_01_00.mp4"
                data-caption-path="media/captions/LM_01_00.vtt">Remote Desktop Protocol</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_01_01.mp4"
                        data-media-path="media/video/LM_01_01.mp4"
                        data-caption-path="media/captions/LM_01_01.vtt">Lateral Movement with RDP</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_01_02.mp4"
                        data-media-path="media/video/LM_01_02.mp4"
                        data-caption-path="media/captions/LM_01_02.vtt">Reverse RDP Proxying With Metasploit</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_01_03.mp4"
                        data-media-path="media/video/LM_01_03.mp4"
                        data-caption-path="media/captions/LM_01_03.vtt">Reverse RDP Proxying With Chisel</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_01_04.mp4"
                        data-media-path="media/video/LM_01_04.mp4"
                        data-caption-path="media/captions/LM_01_04.vtt">RDP as a Console</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_01_05.mp4"
                        data-media-path="media/video/LM_01_05.mp4"
                        data-caption-path="media/captions/LM_01_05.vtt">Stealing Clear Text Credentials From RDP</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LM_02_00.mp4"
                data-media-path="media/video/LM_02_00.mp4"
                data-caption-path="media/captions/LM_02_00.vtt">Fileless Lateral Movement</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_02_01.mp4"
                        data-media-path="media/video/LM_02_01.mp4"
                        data-caption-path="media/captions/LM_02_01.vtt">Authentication and Execution Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LM_02_02.mp4"
                        data-media-path="media/video/LM_02_02.mp4"
                        data-caption-path="media/captions/LM_02_02.vtt">Implementing Fileless Lateral Movement in C#</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LM_03_00.mp4"
                data-media-path="media/video/LM_03_00.mp4"
                data-caption-path="media/captions/LM_03_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/LLM_00_00.mp4"
        data-media-path="media/video/LLM_00_00.mp4" data-caption-path="media/captions/LLM_00_00.vtt">Linux Lateral Movement</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LLM_01_00.mp4"
                data-media-path="media/video/LLM_01_00.mp4"
                data-caption-path="media/captions/LLM_01_00.vtt">Lateral Movement with SSH</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_01_01.mp4"
                        data-media-path="media/video/LLM_01_01.mp4"
                        data-caption-path="media/captions/LLM_01_01.vtt">SSH Keys</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_01_02.mp4"
                        data-media-path="media/video/LLM_01_02.mp4"
                        data-caption-path="media/captions/LLM_01_02.vtt">SSH Persistence</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_01_03.mp4"
                        data-media-path="media/video/LLM_01_03.mp4"
                        data-caption-path="media/captions/LLM_01_03.vtt">SSH Hijacking with ControlMaster</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_01_04.mp4"
                        data-media-path="media/video/LLM_01_04.mp4"
                        data-caption-path="media/captions/LLM_01_04.vtt">SSH Hijacking Using SSH-Agent and Agent Forwarding</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LLM_02_00.mp4"
                data-media-path="media/video/LLM_02_00.mp4"
                data-caption-path="media/captions/LLM_02_00.vtt">DevOps</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_01.mp4"
                        data-media-path="media/video/LLM_02_01.mp4"
                        data-caption-path="media/captions/LLM_02_01.vtt">Introduction to Ansible</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_02.mp4"
                        data-media-path="media/video/LLM_02_02.mp4"
                        data-caption-path="media/captions/LLM_02_02.vtt">Enumerating Ansible</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_03.mp4"
                        data-media-path="media/video/LLM_02_03.mp4"
                        data-caption-path="media/captions/LLM_02_03.vtt">Ad-hoc Commands</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_04.mp4"
                        data-media-path="media/video/LLM_02_04.mp4"
                        data-caption-path="media/captions/LLM_02_04.vtt">Ansible Playbooks</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_05.mp4"
                        data-media-path="media/video/LLM_02_05.mp4"
                        data-caption-path="media/captions/LLM_02_05.vtt">Sensitive Data Leakage via Ansible Modules</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_06.mp4"
                        data-media-path="media/video/LLM_02_06.mp4"
                        data-caption-path="media/captions/LLM_02_06.vtt">Introduction to Artifactory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_07.mp4"
                        data-media-path="media/video/LLM_02_07.mp4"
                        data-caption-path="media/captions/LLM_02_07.vtt">Artifactory Enumeration</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_08.mp4"
                        data-media-path="media/video/LLM_02_08.mp4"
                        data-caption-path="media/captions/LLM_02_08.vtt">Compromising Artifactory Backups</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_09.mp4"
                        data-media-path="media/video/LLM_02_09.mp4"
                        data-caption-path="media/captions/LLM_02_09.vtt">Compromising Artifactory's Database</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_02_10.mp4"
                        data-media-path="media/video/LLM_02_10.mp4"
                        data-caption-path="media/captions/LLM_02_10.vtt">Adding a Secondary Artifactory Admin Account</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LLM_03_00.mp4"
                data-media-path="media/video/LLM_03_00.mp4"
                data-caption-path="media/captions/LLM_03_00.vtt">Kerberos on Linux</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_03_01.mp4"
                        data-media-path="media/video/LLM_03_01.mp4"
                        data-caption-path="media/captions/LLM_03_01.vtt">General Introduction to Kerberos on Linux</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_03_02.mp4"
                        data-media-path="media/video/LLM_03_02.mp4"
                        data-caption-path="media/captions/LLM_03_02.vtt">Stealing Keytab Files</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_03_03.mp4"
                        data-media-path="media/video/LLM_03_03.mp4"
                        data-caption-path="media/captions/LLM_03_03.vtt">Attacking Using Credential Cache Files</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/LLM_03_04.mp4"
                        data-media-path="media/video/LLM_03_04.mp4"
                        data-caption-path="media/captions/LLM_03_04.vtt">Using Kerberos with Impacket</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/LLM_04_00.mp4"
                data-media-path="media/video/LLM_04_00.mp4"
                data-caption-path="media/captions/LLM_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/MSSQL_00_00.mp4"
        data-media-path="media/video/MSSQL_00_00.mp4"
        data-caption-path="media/captions/MSSQL_00_00.vtt">Microsoft SQL Attacks</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/MSSQL_01_00.mp4"
                data-media-path="media/video/MSSQL_01_00.mp4"
                data-caption-path="media/captions/MSSQL_01_00.vtt">MS SQL in Active Directory</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_01_01.mp4"
                        data-media-path="media/video/MSSQL_01_01.mp4"
                        data-caption-path="media/captions/MSSQL_01_01.vtt">MS SQL Enumeration</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_01_02.mp4"
                        data-media-path="media/video/MSSQL_01_02.mp4"
                        data-caption-path="media/captions/MSSQL_01_02.vtt">MS SQL Authentication</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_01_03.mp4"
                        data-media-path="media/video/MSSQL_01_03.mp4"
                        data-caption-path="media/captions/MSSQL_01_03.vtt">UNC Path Injection</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_01_04.mp4"
                        data-media-path="media/video/MSSQL_01_04.mp4"
                        data-caption-path="media/captions/MSSQL_01_04.vtt">Relay My Hash</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/MSSQL_02_00.mp4"
                data-media-path="media/video/MSSQL_02_00.mp4"
                data-caption-path="media/captions/MSSQL_02_00.vtt">MS SQL Escalation</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_02_01.mp4"
                        data-media-path="media/video/MSSQL_02_01.mp4"
                        data-caption-path="media/captions/MSSQL_02_01.vtt">Privilege Escalation</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_02_02.mp4"
                        data-media-path="media/video/MSSQL_02_02.mp4"
                        data-caption-path="media/captions/MSSQL_02_02.vtt">Getting Code Execution</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_02_03.mp4"
                        data-media-path="media/video/MSSQL_02_03.mp4"
                        data-caption-path="media/captions/MSSQL_02_03.vtt">Custom Assemblies</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/MSSQL_03_00.mp4"
                data-media-path="media/video/MSSQL_03_00.mp4"
                data-caption-path="media/captions/MSSQL_03_00.vtt">Linked SQL Servers</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_03_01.mp4"
                        data-media-path="media/video/MSSQL_03_01.mp4"
                        data-caption-path="media/captions/MSSQL_03_01.vtt">Follow The Link</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/MSSQL_03_02.mp4"
                        data-media-path="media/video/MSSQL_03_02.mp4"
                        data-caption-path="media/captions/MSSQL_03_02.vtt">Come Home To Me</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/MSSQL_04_00.mp4"
                data-media-path="media/video/MSSQL_04_00.mp4"
                data-caption-path="media/captions/MSSQL_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/AD_00_00.mp4"
        data-media-path="media/video/AD_00_00.mp4" data-caption-path="media/captions/AD_00_00.vtt">Active Directory Exploitation</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_01_00.mp4"
                data-media-path="media/video/AD_01_00.mp4" data-caption-path="media/captions/AD_01_00.vtt">AD
                Object Security Permissions</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_01_01.mp4"
                        data-media-path="media/video/AD_01_01.mp4"
                        data-caption-path="media/captions/AD_01_01.vtt">Object Permission Theory</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_01_02.mp4"
                        data-media-path="media/video/AD_01_02.mp4"
                        data-caption-path="media/captions/AD_01_02.vtt">Abusing GenericAll</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_01_03.mp4"
                        data-media-path="media/video/AD_01_03.mp4"
                        data-caption-path="media/captions/AD_01_03.vtt">Abusing WriteDACL</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_02_00.mp4"
                data-media-path="media/video/AD_02_00.mp4"
                data-caption-path="media/captions/AD_02_00.vtt">Kerberos Delegation</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_02_01.mp4"
                        data-media-path="media/video/AD_02_01.mp4"
                        data-caption-path="media/captions/AD_02_01.vtt">Unconstrained Delegation</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_02_02.mp4"
                        data-media-path="media/video/AD_02_02.mp4"
                        data-caption-path="media/captions/AD_02_02.vtt">I Am a Domain Controller</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_02_03.mp4"
                        data-media-path="media/video/AD_02_03.mp4"
                        data-caption-path="media/captions/AD_02_03.vtt">Constrained Delegation</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_02_04.mp4"
                        data-media-path="media/video/AD_02_04.mp4"
                        data-caption-path="media/captions/AD_02_04.vtt">Resource-Based Constrained Delegation</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_03_00.mp4"
                data-media-path="media/video/AD_03_00.mp4"
                data-caption-path="media/captions/AD_03_00.vtt">Active Directory Forest Theory</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_03_01.mp4"
                        data-media-path="media/video/AD_03_01.mp4"
                        data-caption-path="media/captions/AD_03_01.vtt">Active Directory Trust in a Forest</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_03_02.mp4"
                        data-media-path="media/video/AD_03_02.mp4"
                        data-caption-path="media/captions/AD_03_02.vtt">Enumeration in the Forest</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_04_00.mp4"
                data-media-path="media/video/AD_04_00.mp4"
                data-caption-path="media/captions/AD_04_00.vtt">Burning Down the Forest</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_04_01.mp4"
                        data-media-path="media/video/AD_04_01.mp4"
                        data-caption-path="media/captions/AD_04_01.vtt">Owning the Forest with Extra SIDs</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_04_02.mp4"
                        data-media-path="media/video/AD_04_02.mp4"
                        data-caption-path="media/captions/AD_04_02.vtt">Owning the Forest with Printers</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_05_00.mp4"
                data-media-path="media/video/AD_05_00.mp4" data-caption-path="media/captions/AD_05_00.vtt">Going Beyond the Forest</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_05_01.mp4"
                        data-media-path="media/video/AD_05_01.mp4"
                        data-caption-path="media/captions/AD_05_01.vtt">Active Directory Trust Between Forests</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_05_02.mp4"
                        data-media-path="media/video/AD_05_02.mp4"
                        data-caption-path="media/captions/AD_05_02.vtt">Enumeration Beyond the Forest</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_06_00.mp4"
                data-media-path="media/video/AD_06_00.mp4"
                data-caption-path="media/captions/AD_06_00.vtt">Compromising an Additional Forest</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_06_01.mp4"
                        data-media-path="media/video/AD_06_01.mp4"
                        data-caption-path="media/captions/AD_06_01.vtt">Show Me Your Extra SID</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/AD_06_02.mp4"
                        data-media-path="media/video/AD_06_02.mp4"
                        data-caption-path="media/captions/AD_06_02.vtt">Linked SQL Servers in the Forest</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/AD_07_00.mp4"
                data-media-path="media/video/AD_07_00.mp4"
                data-caption-path="media/captions/AD_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
        href="https://pen300.hide01.ir/media/video/CTP_00_00.mp4"
        data-media-path="media/video/CTP_00_00.mp4" data-caption-path="media/captions/CTP_00_00.vtt">Combining the Pieces</a>
        <ul class="submenu">
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CTP_01_00.mp4"
                data-media-path="media/video/CTP_01_00.mp4"
                data-caption-path="media/captions/CTP_01_00.vtt">Enumeration and Shell</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_01_01.mp4"
                        data-media-path="media/video/CTP_01_01.mp4"
                        data-caption-path="media/captions/CTP_01_01.vtt">Initial Enumeration</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_01_02.mp4"
                        data-media-path="media/video/CTP_01_02.mp4"
                        data-caption-path="media/captions/CTP_01_02.vtt">Gaining an Initial Foothold</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_01_03.mp4"
                        data-media-path="media/video/CTP_01_03.mp4"
                        data-caption-path="media/captions/CTP_01_03.vtt">Post Exploitation Enumeration</a>
                </li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CTP_02_00.mp4"
                data-media-path="media/video/CTP_02_00.mp4"
                data-caption-path="media/captions/CTP_02_00.vtt">Attacking Delegation</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_02_01.mp4"
                        data-media-path="media/video/CTP_02_01.mp4"
                        data-caption-path="media/captions/CTP_02_01.vtt">Privilege Escalation on web01</a>
                </li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_02_02.mp4"
                        data-media-path="media/video/CTP_02_02.mp4"
                        data-caption-path="media/captions/CTP_02_02.vtt">Getting the Hash</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_02_03.mp4"
                        data-media-path="media/video/CTP_02_03.mp4"
                        data-caption-path="media/captions/CTP_02_03.vtt">Delegate My Ticket</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CTP_03_00.mp4"
                data-media-path="media/video/CTP_03_00.mp4"
                data-caption-path="media/captions/CTP_03_00.vtt">Owning the Domain</a></li>
        <ul class="subSection-menu">
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_03_01.mp4"
                        data-media-path="media/video/CTP_03_01.mp4"
                        data-caption-path="media/captions/CTP_03_01.vtt">Lateral Movement</a></li>
                <li><a class="sub-module"
                        href="https://pen300.hide01.ir/media/video/CTP_03_02.mp4"
                        data-media-path="media/video/CTP_03_02.mp4"
                        data-caption-path="media/captions/CTP_03_02.vtt">Becoming Domain Admin</a></li>
        </ul>
        <li><a class="sub-module"
                href="https://pen300.hide01.ir/media/video/CTP_04_00.mp4"
                data-media-path="media/video/CTP_04_00.mp4"
                data-caption-path="media/captions/CTP_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
"""
soup = BeautifulSoup(html_code, 'html.parser')
data = []

modules = soup.find_all('li', class_='module-title')
for module in modules:
    modules_dict = {}
    modules_dict["Module"] = (module.find('a', class_='module').text)
    modules_dict["Href"] = (module.find('a', class_='module')['href'])
    submodule_list = module.find('ul', class_='submenu')
    if submodule_list:
        submodules = submodule_list.find_all('li')
        submodule_list = []
        for submodule in submodules:
            tempDict = {}
            tempDict["Submodule"] = (submodule.find('a', class_='sub-module').text)
            sub_submodule_list = submodule.find('ul', class_='subSection-menu')
            if sub_submodule_list:
                sub_submodules = sub_submodule_list.find_all('li')
                for sub_submodule in sub_submodules:
                    tempDict["Sub-Submodule"] = (sub_submodule.find('a', class_='sub-module').text)
                    tempDict["Href"] = (sub_submodule.find('a', class_='sub-module')['href'])
            else:
                tempDict["Href"] = submodule.find('a', class_='sub-module')['href']
            submodule_list.append(tempDict)
    modules_dict["Submodules"] = submodule_list
    # json_data = json.dumps(modules_dict)
    # print(json_data)
    # data.append(json_data)
    data.append(modules_dict)
    
json_data = json.dumps(data)

with open('data.json', 'w') as f:
    f.write(json_data)

print("JSON data has been written to data.json")



# Creating directories 
import os
import urllib.request

# Loop through the data and create directories and download files
for module_data in data:
    module_name = module_data['Module']
    submodules = module_data['Submodules']
    
    # Create directory for module
    os.makedirs(module_name, exist_ok=True)

    # Loop through submodules
    for submodule in submodules:
        submodule_name = submodule['Submodule']
        href = submodule['Href']
        print(href)
        
        # Create directory for submodule
        submodule_path = os.path.join(module_name, submodule_name)
        os.makedirs(submodule_path, exist_ok=True)
        
        # # Download file from href
        # if href:
        file_name = os.path.basename(href)
        file_path = os.path.join(submodule_path, file_name)
        urllib.request.urlretrieve(href, file_path)
        print(f"Downloaded file: {file_name} to {submodule_path}")
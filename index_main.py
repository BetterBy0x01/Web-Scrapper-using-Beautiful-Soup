from bs4 import BeautifulSoup
import json

html_code = """
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/GCKL_00_00.mp4"
                data-media-path="media/video/GCKL_00_00.mp4" data-caption-path="media/captions/GCKL_00_00.vtt">Getting Comfortable with Kali Linux</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_01_00.mp4"
                                data-media-path="media/video/GCKL_01_00.mp4"
                                data-caption-path="media/captions/GCKL_01_00.vtt">Booting Up Kali Linux</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_02_00.mp4"
                                data-media-path="media/video/GCKL_02_00.mp4"
                                data-caption-path="media/captions/GCKL_02_00.vtt">The Kali Menu</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_03_00.mp4"
                                data-media-path="media/video/GCKL_03_00.mp4"
                                data-caption-path="media/captions/GCKL_03_00.vtt">Kali Documentation</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_04_00.mp4"
                                data-media-path="media/video/GCKL_04_00.mp4"
                                data-caption-path="media/captions/GCKL_04_00.vtt">Finding Your Way Around Kali</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_04_01.mp4"
                                        data-media-path="media/video/GCKL_04_01.mp4"
                                        data-caption-path="media/captions/GCKL_04_01.vtt">The Linux Filesystem</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_04_02.mp4"
                                        data-media-path="media/video/GCKL_04_02.mp4"
                                        data-caption-path="media/captions/GCKL_04_02.vtt">Basic Linux Commands</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_04_03.mp4"
                                        data-media-path="media/video/GCKL_04_03.mp4"
                                        data-caption-path="media/captions/GCKL_04_03.vtt">Finding Files in Kali Linux</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_05_00.mp4"
                                data-media-path="media/video/GCKL_05_00.mp4"
                                data-caption-path="media/captions/GCKL_05_00.vtt">Managing Kali Linux Services</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_05_01.mp4"
                                        data-media-path="media/video/GCKL_05_01.mp4"
                                        data-caption-path="media/captions/GCKL_05_01.vtt">SSH Service</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_05_02.mp4"
                                        data-media-path="media/video/GCKL_05_02.mp4"
                                        data-caption-path="media/captions/GCKL_05_02.vtt">HTTP Service</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_00.mp4"
                                data-media-path="media/video/GCKL_06_00.mp4"
                                data-caption-path="media/captions/GCKL_06_00.vtt">Searching, Installing, and Removing Tools</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_01.mp4"
                                        data-media-path="media/video/GCKL_06_01.mp4"
                                        data-caption-path="media/captions/GCKL_06_01.vtt">apt update</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_02.mp4"
                                        data-media-path="media/video/GCKL_06_02.mp4"
                                        data-caption-path="media/captions/GCKL_06_02.vtt">apt upgrade</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_03.mp4"
                                        data-media-path="media/video/GCKL_06_03.mp4"
                                        data-caption-path="media/captions/GCKL_06_03.vtt">apt-cache search and apt show</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_04.mp4"
                                        data-media-path="media/video/GCKL_06_04.mp4"
                                        data-caption-path="media/captions/GCKL_06_04.vtt">apt install</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_05.mp4"
                                        data-media-path="media/video/GCKL_06_05.mp4"
                                        data-caption-path="media/captions/GCKL_06_05.vtt">apt remove --purge</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_06_06.mp4"
                                        data-media-path="media/video/GCKL_06_06.mp4"
                                        data-caption-path="media/captions/GCKL_06_06.vtt">dpkg</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/GCKL_07_00.mp4"
                                data-media-path="media/video/GCKL_07_00.mp4"
                                data-caption-path="media/captions/GCKL_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/CLF_00_00.mp4"
                data-media-path="media/video/CLF_00_00.mp4" data-caption-path="media/captions/CLF_00_00.vtt">Command Line Fun</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_01_00.mp4"
                                data-media-path="media/video/CLF_01_00.mp4"
                                data-caption-path="media/captions/CLF_01_00.vtt">The Bash Environment</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_01_01.mp4"
                                        data-media-path="media/video/CLF_01_01.mp4"
                                        data-caption-path="media/captions/CLF_01_01.vtt">Environment Variables</a></li>
                        <li><a class="sub-module active" href="https://pwk.hide01.ir/media/video/CLF_01_02.mp4"
                                        data-media-path="media/video/CLF_01_02.mp4"
                                        data-caption-path="media/captions/CLF_01_02.vtt">Tab Completion</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_01_03.mp4"
                                        data-media-path="media/video/CLF_01_03.mp4"
                                        data-caption-path="media/captions/CLF_01_03.vtt">Bash History Tricks</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_00.mp4"
                                data-media-path="media/video/CLF_02_00.mp4"
                                data-caption-path="media/captions/CLF_02_00.vtt">Piping and Redirection</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_01.mp4"
                                        data-media-path="media/video/CLF_02_01.mp4"
                                        data-caption-path="media/captions/CLF_02_01.vtt">Redirecting to a New File</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_02.mp4"
                                        data-media-path="media/video/CLF_02_02.mp4"
                                        data-caption-path="media/captions/CLF_02_02.vtt">Redirecting to an Existing File</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_03.mp4"
                                        data-media-path="media/video/CLF_02_03.mp4"
                                        data-caption-path="media/captions/CLF_02_03.vtt">Redirecting from a File</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_04.mp4"
                                        data-media-path="media/video/CLF_02_04.mp4"
                                        data-caption-path="media/captions/CLF_02_04.vtt">Redirecting STDERR</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_02_05.mp4"
                                        data-media-path="media/video/CLF_02_05.mp4"
                                        data-caption-path="media/captions/CLF_02_05.vtt">Piping</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_00.mp4"
                                data-media-path="media/video/CLF_03_00.mp4"
                                data-caption-path="media/captions/CLF_03_00.vtt">Text Searching and Manipulation</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_01.mp4"
                                        data-media-path="media/video/CLF_03_01.mp4"
                                        data-caption-path="media/captions/CLF_03_01.vtt">grep</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_02.mp4"
                                        data-media-path="media/video/CLF_03_02.mp4"
                                        data-caption-path="media/captions/CLF_03_02.vtt">sed</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_03.mp4"
                                        data-media-path="media/video/CLF_03_03.mp4"
                                        data-caption-path="media/captions/CLF_03_03.vtt">cut</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_04.mp4"
                                        data-media-path="media/video/CLF_03_04.mp4"
                                        data-caption-path="media/captions/CLF_03_04.vtt">awk</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_03_05.mp4"
                                        data-media-path="media/video/CLF_03_05.mp4"
                                        data-caption-path="media/captions/CLF_03_05.vtt">Practical Example</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_04_00.mp4"
                                data-media-path="media/video/CLF_04_00.mp4"
                                data-caption-path="media/captions/CLF_04_00.vtt">Editing Files from the Command Line</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_04_01.mp4"
                                        data-media-path="media/video/CLF_04_01.mp4"
                                        data-caption-path="media/captions/CLF_04_01.vtt">nano</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_04_02.mp4"
                                        data-media-path="media/video/CLF_04_02.mp4"
                                        data-caption-path="media/captions/CLF_04_02.vtt">vi</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_05_00.mp4"
                                data-media-path="media/video/CLF_05_00.mp4"
                                data-caption-path="media/captions/CLF_05_00.vtt">Comparing Files</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_05_01.mp4"
                                        data-media-path="media/video/CLF_05_01.mp4"
                                        data-caption-path="media/captions/CLF_05_01.vtt">comm</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_05_02.mp4"
                                        data-media-path="media/video/CLF_05_02.mp4"
                                        data-caption-path="media/captions/CLF_05_02.vtt">diff</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_05_03.mp4"
                                        data-media-path="media/video/CLF_05_03.mp4"
                                        data-caption-path="media/captions/CLF_05_03.vtt">vimdiff</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_06_00.mp4"
                                data-media-path="media/video/CLF_06_00.mp4"
                                data-caption-path="media/captions/CLF_06_00.vtt">Managing Processes</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_06_01.mp4"
                                        data-media-path="media/video/CLF_06_01.mp4"
                                        data-caption-path="media/captions/CLF_06_01.vtt">Backgrounding Processes (bg)</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_06_02.mp4"
                                        data-media-path="media/video/CLF_06_02.mp4"
                                        data-caption-path="media/captions/CLF_06_02.vtt">Jobs Control: jobs and fg</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_06_03.mp4"
                                        data-media-path="media/video/CLF_06_03.mp4"
                                        data-caption-path="media/captions/CLF_06_03.vtt">Process Control: ps and kill</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_07_00.mp4"
                                data-media-path="media/video/CLF_07_00.mp4"
                                data-caption-path="media/captions/CLF_07_00.vtt">File and Command Monitoring</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_07_01.mp4"
                                        data-media-path="media/video/CLF_07_01.mp4"
                                        data-caption-path="media/captions/CLF_07_01.vtt">tail</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_07_02.mp4"
                                        data-media-path="media/video/CLF_07_02.mp4"
                                        data-caption-path="media/captions/CLF_07_02.vtt">watch</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_08_00.mp4"
                                data-media-path="media/video/CLF_08_00.mp4"
                                data-caption-path="media/captions/CLF_08_00.vtt">Downloading Files</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_08_01.mp4"
                                        data-media-path="media/video/CLF_08_01.mp4"
                                        data-caption-path="media/captions/CLF_08_01.vtt">wget</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_08_02.mp4"
                                        data-media-path="media/video/CLF_08_02.mp4"
                                        data-caption-path="media/captions/CLF_08_02.vtt">curl</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_08_03.mp4"
                                        data-media-path="media/video/CLF_08_03.mp4"
                                        data-caption-path="media/captions/CLF_08_03.vtt">axel</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_09_00.mp4"
                                data-media-path="media/video/CLF_09_00.mp4"
                                data-caption-path="media/captions/CLF_09_00.vtt">Customizing the Bash Environment</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_09_01.mp4"
                                        data-media-path="media/video/CLF_09_01.mp4"
                                        data-caption-path="media/captions/CLF_09_01.vtt">Bash History Customization</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_09_02.mp4"
                                        data-media-path="media/video/CLF_09_02.mp4"
                                        data-caption-path="media/captions/CLF_09_02.vtt">Alias</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_09_03.mp4"
                                        data-media-path="media/video/CLF_09_03.mp4"
                                        data-caption-path="media/captions/CLF_09_03.vtt">Persistent Bash Customization</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CLF_10_00.mp4"
                                data-media-path="media/video/CLF_10_00.mp4"
                                data-caption-path="media/captions/CLF_10_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PT_00_00.mp4"
                data-media-path="media/video/PT_00_00.mp4" data-caption-path="media/captions/PT_00_00.vtt">Practical Tools</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_01_00.mp4"
                                data-media-path="media/video/PT_01_00.mp4"
                                data-caption-path="media/captions/PT_01_00.vtt">Netcat</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_01_01.mp4"
                                        data-media-path="media/video/PT_01_01.mp4"
                                        data-caption-path="media/captions/PT_01_01.vtt">Connecting to a TCP/UDP Port</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_01_02.mp4"
                                        data-media-path="media/video/PT_01_02.mp4"
                                        data-caption-path="media/captions/PT_01_02.vtt">Listening on a TCP/UDP Port</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_01_03.mp4"
                                        data-media-path="media/video/PT_01_03.mp4"
                                        data-caption-path="media/captions/PT_01_03.vtt">Transferring Files with Netcat</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_01_04.mp4"
                                        data-media-path="media/video/PT_01_04.mp4"
                                        data-caption-path="media/captions/PT_01_04.vtt">Remote Administration with Netcat</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_02_00.mp4"
                                data-media-path="media/video/PT_02_00.mp4"
                                data-caption-path="media/captions/PT_02_00.vtt">Socat</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_02_01.mp4"
                                        data-media-path="media/video/PT_02_01.mp4"
                                        data-caption-path="media/captions/PT_02_01.vtt">Socat File Transfers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_02_02.mp4"
                                        data-media-path="media/video/PT_02_02.mp4"
                                        data-caption-path="media/captions/PT_02_02.vtt">Socat Reverse Shells</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_02_03.mp4"
                                        data-media-path="media/video/PT_02_03.mp4"
                                        data-caption-path="media/captions/PT_02_03.vtt">Socat Encrypted Bind Shells</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_00.mp4"
                                data-media-path="media/video/PT_03_00.mp4"
                                data-caption-path="media/captions/PT_03_00.vtt">PowerShell and Powercat</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_01.mp4"
                                        data-media-path="media/video/PT_03_01.mp4"
                                        data-caption-path="media/captions/PT_03_01.vtt">PowerShell File Transfers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_02.mp4"
                                        data-media-path="media/video/PT_03_02.mp4"
                                        data-caption-path="media/captions/PT_03_02.vtt">PowerShell Reverse Shells</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_03.mp4"
                                        data-media-path="media/video/PT_03_03.mp4"
                                        data-caption-path="media/captions/PT_03_03.vtt">PowerShell Bind Shells</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_04.mp4"
                                        data-media-path="media/video/PT_03_04.mp4"
                                        data-caption-path="media/captions/PT_03_04.vtt">Powercat</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_05.mp4"
                                        data-media-path="media/video/PT_03_05.mp4"
                                        data-caption-path="media/captions/PT_03_05.vtt">Powercat File Transfers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_06.mp4"
                                        data-media-path="media/video/PT_03_06.mp4"
                                        data-caption-path="media/captions/PT_03_06.vtt">Powercat Reverse Shells</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_07.mp4"
                                        data-media-path="media/video/PT_03_07.mp4"
                                        data-caption-path="media/captions/PT_03_07.vtt">Powercat Bind Shells</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_03_08.mp4"
                                        data-media-path="media/video/PT_03_08.mp4"
                                        data-caption-path="media/captions/PT_03_08.vtt">Powercat Stand-Alone Payloads</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_00.mp4"
                                data-media-path="media/video/PT_04_00.mp4"
                                data-caption-path="media/captions/PT_04_00.vtt">Wireshark</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_01.mp4"
                                        data-media-path="media/video/PT_04_01.mp4"
                                        data-caption-path="media/captions/PT_04_01.vtt">Wireshark Basics</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_02.mp4"
                                        data-media-path="media/video/PT_04_02.mp4"
                                        data-caption-path="media/captions/PT_04_02.vtt">Launching Wireshark</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_03.mp4"
                                        data-media-path="media/video/PT_04_03.mp4"
                                        data-caption-path="media/captions/PT_04_03.vtt">Capture Filters</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_04.mp4"
                                        data-media-path="media/video/PT_04_04.mp4"
                                        data-caption-path="media/captions/PT_04_04.vtt">Display Filters</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_04_05.mp4"
                                        data-media-path="media/video/PT_04_05.mp4"
                                        data-caption-path="media/captions/PT_04_05.vtt">Following TCP Streams</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_05_00.mp4"
                                data-media-path="media/video/PT_05_00.mp4"
                                data-caption-path="media/captions/PT_05_00.vtt">Tcpdump</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_05_01.mp4"
                                        data-media-path="media/video/PT_05_01.mp4"
                                        data-caption-path="media/captions/PT_05_01.vtt">Filtering Traffic</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PT_05_02.mp4"
                                        data-media-path="media/video/PT_05_02.mp4"
                                        data-caption-path="media/captions/PT_05_02.vtt">Advanced Header Filtering</a></li>
                </ul>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/BS_00_00.mp4"
                data-media-path="media/video/BS_00_00.mp4" data-caption-path="media/captions/BS_00_00.vtt">Bash Scripting</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_01_00.mp4"
                                data-media-path="media/video/BS_01_00.mp4"
                                data-caption-path="media/captions/BS_01_00.vtt">Intro to Bash Scripting</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_02_00.mp4"
                                data-media-path="media/video/BS_02_00.mp4"
                                data-caption-path="media/captions/BS_02_00.vtt">Variables</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_02_01.mp4"
                                        data-media-path="media/video/BS_02_01.mp4"
                                        data-caption-path="media/captions/BS_02_01.vtt">Arguments</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_02_02.mp4"
                                        data-media-path="media/video/BS_02_02.mp4"
                                        data-caption-path="media/captions/BS_02_02.vtt">Reading User Input</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_03_00.mp4"
                                data-media-path="media/video/BS_03_00.mp4"
                                data-caption-path="media/captions/BS_03_00.vtt">If, Else, Elif Statements</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_04_00.mp4"
                                data-media-path="media/video/BS_04_00.mp4"
                                data-caption-path="media/captions/BS_04_00.vtt">Boolean Logical Operations</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_05_00.mp4"
                                data-media-path="media/video/BS_05_00.mp4"
                                data-caption-path="media/captions/BS_05_00.vtt">Loops</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_05_01.mp4"
                                        data-media-path="media/video/BS_05_01.mp4"
                                        data-caption-path="media/captions/BS_05_01.vtt">For Loops</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_05_02.mp4"
                                        data-media-path="media/video/BS_05_02.mp4"
                                        data-caption-path="media/captions/BS_05_02.vtt">While Loops</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_06_00.mp4"
                                data-media-path="media/video/BS_06_00.mp4"
                                data-caption-path="media/captions/BS_06_00.vtt">Functions</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_07_00.mp4"
                                data-media-path="media/video/BS_07_00.mp4"
                                data-caption-path="media/captions/BS_07_00.vtt">Practical Examples</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_07_01.mp4"
                                        data-media-path="media/video/BS_07_01.mp4"
                                        data-caption-path="media/captions/BS_07_01.vtt">Practical Bash Usage  Example 1</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_07_02.mp4"
                                        data-media-path="media/video/BS_07_02.mp4"
                                        data-caption-path="media/captions/BS_07_02.vtt">Practical Bash Usage  Example 2</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BS_07_03.mp4"
                                        data-media-path="media/video/BS_07_03.mp4"
                                        data-caption-path="media/captions/BS_07_03.vtt">Practical Bash Usage  Example 3</a></li>
                </ul>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PIG_00_00.mp4"
                data-media-path="media/video/PIG_00_00.mp4" data-caption-path="media/captions/PIG_00_00.vtt">Passive Information Gathering</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_01_00.mp4"
                                data-media-path="media/video/PIG_01_00.mp4"
                                data-caption-path="media/captions/PIG_01_00.vtt">Website Recon</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_02_00.mp4"
                                data-media-path="media/video/PIG_02_00.mp4"
                                data-caption-path="media/captions/PIG_02_00.vtt">Whois Enumeration</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_03_00.mp4"
                                data-media-path="media/video/PIG_03_00.mp4"
                                data-caption-path="media/captions/PIG_03_00.vtt">Google Hacking</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_04_00.mp4"
                                data-media-path="media/video/PIG_04_00.mp4"
                                data-caption-path="media/captions/PIG_04_00.vtt">Netcraft</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_05_00.mp4"
                                data-media-path="media/video/PIG_05_00.mp4"
                                data-caption-path="media/captions/PIG_05_00.vtt">Recon-ng</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_06_00.mp4"
                                data-media-path="media/video/PIG_06_00.mp4"
                                data-caption-path="media/captions/PIG_06_00.vtt">Open-Source Code</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_07_00.mp4"
                                data-media-path="media/video/PIG_07_00.mp4"
                                data-caption-path="media/captions/PIG_07_00.vtt">Shodan</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_08_00.mp4"
                                data-media-path="media/video/PIG_08_00.mp4"
                                data-caption-path="media/captions/PIG_08_00.vtt">Security Headers Scanner</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_09_00.mp4"
                                data-media-path="media/video/PIG_09_00.mp4"
                                data-caption-path="media/captions/PIG_09_00.vtt">SSL Server Test</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_10_00.mp4"
                                data-media-path="media/video/PIG_10_00.mp4"
                                data-caption-path="media/captions/PIG_10_00.vtt">Pastebin</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_11_00.mp4"
                                data-media-path="media/video/PIG_11_00.mp4"
                                data-caption-path="media/captions/PIG_11_00.vtt">User Information Gathering</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_11_01.mp4"
                                        data-media-path="media/video/PIG_11_01.mp4"
                                        data-caption-path="media/captions/PIG_11_01.vtt">Email Harvesting</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_11_02.mp4"
                                        data-media-path="media/video/PIG_11_02.mp4"
                                        data-caption-path="media/captions/PIG_11_02.vtt">Password Dumps</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_12_00.mp4"
                                data-media-path="media/video/PIG_12_00.mp4"
                                data-caption-path="media/captions/PIG_12_00.vtt">Social Media Tools</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_12_01.mp4"
                                        data-media-path="media/video/PIG_12_01.mp4"
                                        data-caption-path="media/captions/PIG_12_01.vtt">Site-Specific Tools</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_13_00.mp4"
                                data-media-path="media/video/PIG_13_00.mp4"
                                data-caption-path="media/captions/PIG_13_00.vtt">Stack Overflow</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_14_00.mp4"
                                data-media-path="media/video/PIG_14_00.mp4"
                                data-caption-path="media/captions/PIG_14_00.vtt">Information Gathering Frameworks</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_14_01.mp4"
                                        data-media-path="media/video/PIG_14_01.mp4"
                                        data-caption-path="media/captions/PIG_14_01.vtt">OSINT Framework</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_14_02.mp4"
                                        data-media-path="media/video/PIG_14_02.mp4"
                                        data-caption-path="media/captions/PIG_14_02.vtt">Maltego</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PIG_15_00.mp4"
                                data-media-path="media/video/PIG_15_00.mp4"
                                data-caption-path="media/captions/PIG_15_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/AIG_00_00.mp4"
                data-media-path="media/video/AIG_00_00.mp4" data-caption-path="media/captions/AIG_00_00.vtt">Active Information Gathering</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_00.mp4"
                                data-media-path="media/video/AIG_01_00.mp4"
                                data-caption-path="media/captions/AIG_01_00.vtt">DNS Enumeration</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_01.mp4"
                                        data-media-path="media/video/AIG_01_01.mp4"
                                        data-caption-path="media/captions/AIG_01_01.vtt">Interacting with a DNS Server</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_02.mp4"
                                        data-media-path="media/video/AIG_01_02.mp4"
                                        data-caption-path="media/captions/AIG_01_02.vtt">Automating Lookups</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_03.mp4"
                                        data-media-path="media/video/AIG_01_03.mp4"
                                        data-caption-path="media/captions/AIG_01_03.vtt">Forward Lookup Brute Force</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_04.mp4"
                                        data-media-path="media/video/AIG_01_04.mp4"
                                        data-caption-path="media/captions/AIG_01_04.vtt">Reverse Lookup Brute Force</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_05.mp4"
                                        data-media-path="media/video/AIG_01_05.mp4"
                                        data-caption-path="media/captions/AIG_01_05.vtt">DNS Zone Transfers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_01_06.mp4"
                                        data-media-path="media/video/AIG_01_06.mp4"
                                        data-caption-path="media/captions/AIG_01_06.vtt">Relevant Tools in Kali Linux</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_02_00.mp4"
                                data-media-path="media/video/AIG_02_00.mp4"
                                data-caption-path="media/captions/AIG_02_00.vtt">Port Scanning</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_02_01.mp4"
                                        data-media-path="media/video/AIG_02_01.mp4"
                                        data-caption-path="media/captions/AIG_02_01.vtt">TCP/UDP Scanning</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_02_02.mp4"
                                        data-media-path="media/video/AIG_02_02.mp4"
                                        data-caption-path="media/captions/AIG_02_02.vtt">Port Scanning with Nmap</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_02_03.mp4"
                                        data-media-path="media/video/AIG_02_03.mp4"
                                        data-caption-path="media/captions/AIG_02_03.vtt">Masscan</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_03_00.mp4"
                                data-media-path="media/video/AIG_03_00.mp4"
                                data-caption-path="media/captions/AIG_03_00.vtt">SMB Enumeration</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_03_01.mp4"
                                        data-media-path="media/video/AIG_03_01.mp4"
                                        data-caption-path="media/captions/AIG_03_01.vtt">Scanning for the NetBIOS Service</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_03_02.mp4"
                                        data-media-path="media/video/AIG_03_02.mp4"
                                        data-caption-path="media/captions/AIG_03_02.vtt">Nmap SMB NSE Scripts</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_04_00.mp4"
                                data-media-path="media/video/AIG_04_00.mp4"
                                data-caption-path="media/captions/AIG_04_00.vtt">NFS Enumeration</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_04_01.mp4"
                                        data-media-path="media/video/AIG_04_01.mp4"
                                        data-caption-path="media/captions/AIG_04_01.vtt">Scanning for NFS shares</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_04_02.mp4"
                                        data-media-path="media/video/AIG_04_02.mp4"
                                        data-caption-path="media/captions/AIG_04_02.vtt">Nmap NFS NSE Scripts</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_05_00.mp4"
                                data-media-path="media/video/AIG_05_00.mp4"
                                data-caption-path="media/captions/AIG_05_00.vtt">SMTP Enumeration</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_06_00.mp4"
                                data-media-path="media/video/AIG_06_00.mp4"
                                data-caption-path="media/captions/AIG_06_00.vtt">SNMP Enumeration</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_06_01.mp4"
                                        data-media-path="media/video/AIG_06_01.mp4"
                                        data-caption-path="media/captions/AIG_06_01.vtt">The SNMP MIB Tree</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_06_02.mp4"
                                        data-media-path="media/video/AIG_06_02.mp4"
                                        data-caption-path="media/captions/AIG_06_02.vtt">Scanning for SNMP</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_06_03.mp4"
                                        data-media-path="media/video/AIG_06_03.mp4"
                                        data-caption-path="media/captions/AIG_06_03.vtt">Windows SNMP Enumeration Example</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AIG_07_00.mp4"
                                data-media-path="media/video/AIG_07_00.mp4"
                                data-caption-path="media/captions/AIG_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/VS_00_00.mp4"
                data-media-path="media/video/VS_00_00.mp4" data-caption-path="media/captions/VS_00_00.vtt">Vulnerability Scanning</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_01_00.mp4"
                                data-media-path="media/video/VS_01_00.mp4"
                                data-caption-path="media/captions/VS_01_00.vtt">Vulnerability Scanning Overview and Considerations</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_01_01.mp4"
                                        data-media-path="media/video/VS_01_01.mp4"
                                        data-caption-path="media/captions/VS_01_01.vtt">How Vulnerability Scanners Work</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_00.mp4"
                                data-media-path="media/video/VS_02_00.mp4"
                                data-caption-path="media/captions/VS_02_00.vtt">Vulnerability Scanning with Nessus</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_01.mp4"
                                        data-media-path="media/video/VS_02_01.mp4"
                                        data-caption-path="media/captions/VS_02_01.vtt">Installing Nessus</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_02.mp4"
                                        data-media-path="media/video/VS_02_02.mp4"
                                        data-caption-path="media/captions/VS_02_02.vtt">Defining Targets</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_03.mp4"
                                        data-media-path="media/video/VS_02_03.mp4"
                                        data-caption-path="media/captions/VS_02_03.vtt">Configuring Scan Definitions</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_04.mp4"
                                        data-media-path="media/video/VS_02_04.mp4"
                                        data-caption-path="media/captions/VS_02_04.vtt">Unauthenticated Scanning With Nessus</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_05.mp4"
                                        data-media-path="media/video/VS_02_05.mp4"
                                        data-caption-path="media/captions/VS_02_05.vtt">Authenticated Scanning With Nessus</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_02_06.mp4"
                                        data-media-path="media/video/VS_02_06.mp4"
                                        data-caption-path="media/captions/VS_02_06.vtt">Scanning with Individual Nessus Plugins</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_03_00.mp4"
                                data-media-path="media/video/VS_03_00.mp4"
                                data-caption-path="media/captions/VS_03_00.vtt">Vulnerability Scanning with Nmap</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/VS_04_00.mp4"
                                data-media-path="media/video/VS_04_00.mp4"
                                data-caption-path="media/captions/VS_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/WAT_00_00.mp4"
                data-media-path="media/video/WAT_00_00.mp4" data-caption-path="media/captions/WAT_00_00.vtt">Web Application Attacks</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_01_00.mp4"
                                data-media-path="media/video/WAT_01_00.mp4"
                                data-caption-path="media/captions/WAT_01_00.vtt">Web Application Assessment Methodology</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_00.mp4"
                                data-media-path="media/video/WAT_02_00.mp4"
                                data-caption-path="media/captions/WAT_02_00.vtt">Web Application Enumeration</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_01.mp4"
                                        data-media-path="media/video/WAT_02_01.mp4"
                                        data-caption-path="media/captions/WAT_02_01.vtt">Inspecting URLs</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_02.mp4"
                                        data-media-path="media/video/WAT_02_02.mp4"
                                        data-caption-path="media/captions/WAT_02_02.vtt">Inspecting Page Content</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_03.mp4"
                                        data-media-path="media/video/WAT_02_03.mp4"
                                        data-caption-path="media/captions/WAT_02_03.vtt">Viewing Response Headers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_04.mp4"
                                        data-media-path="media/video/WAT_02_04.mp4"
                                        data-caption-path="media/captions/WAT_02_04.vtt">Inspecting Sitemaps</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_02_05.mp4"
                                        data-media-path="media/video/WAT_02_05.mp4"
                                        data-caption-path="media/captions/WAT_02_05.vtt">Locating Administration Consoles</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_03_00.mp4"
                                data-media-path="media/video/WAT_03_00.mp4"
                                data-caption-path="media/captions/WAT_03_00.vtt">Web Application Assessment Tools</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_03_01.mp4"
                                        data-media-path="media/video/WAT_03_01.mp4"
                                        data-caption-path="media/captions/WAT_03_01.vtt">DIRB</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_03_02.mp4"
                                        data-media-path="media/video/WAT_03_02.mp4"
                                        data-caption-path="media/captions/WAT_03_02.vtt">Burp Suite</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_03_03.mp4"
                                        data-media-path="media/video/WAT_03_03.mp4"
                                        data-caption-path="media/captions/WAT_03_03.vtt">Nikto</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_04_00.mp4"
                                data-media-path="media/video/WAT_04_00.mp4"
                                data-caption-path="media/captions/WAT_04_00.vtt">Exploiting Web-based Vulnerabilities</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_05_00.mp4"
                                data-media-path="media/video/WAT_05_00.mp4"
                                data-caption-path="media/captions/WAT_05_00.vtt">Exploiting Admin Consoles</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_05_01.mp4"
                                        data-media-path="media/video/WAT_05_01.mp4"
                                        data-caption-path="media/captions/WAT_05_01.vtt">Burp Suite Intruder</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_06_00.mp4"
                                data-media-path="media/video/WAT_06_00.mp4"
                                data-caption-path="media/captions/WAT_06_00.vtt">Cross-Site Scripting (XSS)</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_06_01.mp4"
                                        data-media-path="media/video/WAT_06_01.mp4"
                                        data-caption-path="media/captions/WAT_06_01.vtt">Identifying XSS Vulnerabilities</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_06_02.mp4"
                                        data-media-path="media/video/WAT_06_02.mp4"
                                        data-caption-path="media/captions/WAT_06_02.vtt">Basic XSS</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_06_03.mp4"
                                        data-media-path="media/video/WAT_06_03.mp4"
                                        data-caption-path="media/captions/WAT_06_03.vtt">Content Injection</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_06_04.mp4"
                                        data-media-path="media/video/WAT_06_04.mp4"
                                        data-caption-path="media/captions/WAT_06_04.vtt">Stealing Cookies and Session Information</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_07_00.mp4"
                                data-media-path="media/video/WAT_07_00.mp4"
                                data-caption-path="media/captions/WAT_07_00.vtt">Directory Traversal Vulnerabilities</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_07_01.mp4"
                                        data-media-path="media/video/WAT_07_01.mp4"
                                        data-caption-path="media/captions/WAT_07_01.vtt">Identifying and Exploiting Directory Traversals</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_00.mp4"
                                data-media-path="media/video/WAT_08_00.mp4"
                                data-caption-path="media/captions/WAT_08_00.vtt">File Inclusion Vulnerabilities</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_01.mp4"
                                        data-media-path="media/video/WAT_08_01.mp4"
                                        data-caption-path="media/captions/WAT_08_01.vtt">Identifying File Inclusion Vulnerabilities</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_02.mp4"
                                        data-media-path="media/video/WAT_08_02.mp4"
                                        data-caption-path="media/captions/WAT_08_02.vtt">Exploiting Local File Inclusion (LFI)</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_03.mp4"
                                        data-media-path="media/video/WAT_08_03.mp4"
                                        data-caption-path="media/captions/WAT_08_03.vtt">Contaminating Log Files</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_04.mp4"
                                        data-media-path="media/video/WAT_08_04.mp4"
                                        data-caption-path="media/captions/WAT_08_04.vtt">LFI Code Execution</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_05.mp4"
                                        data-media-path="media/video/WAT_08_05.mp4"
                                        data-caption-path="media/captions/WAT_08_05.vtt">Remote File Inclusion (RFI)</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_06.mp4"
                                        data-media-path="media/video/WAT_08_06.mp4"
                                        data-caption-path="media/captions/WAT_08_06.vtt">Expanding Your Repertoire</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_08_07.mp4"
                                        data-media-path="media/video/WAT_08_07.mp4"
                                        data-caption-path="media/captions/WAT_08_07.vtt">PHP Wrappers</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_00.mp4"
                                data-media-path="media/video/WAT_09_00.mp4"
                                data-caption-path="media/captions/WAT_09_00.vtt">SQL Injection</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_01.mp4"
                                        data-media-path="media/video/WAT_09_01.mp4"
                                        data-caption-path="media/captions/WAT_09_01.vtt">Basic SQL Syntax</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_02.mp4"
                                        data-media-path="media/video/WAT_09_02.mp4"
                                        data-caption-path="media/captions/WAT_09_02.vtt">Identifying SQL Injection Vulnerabilities</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_03.mp4"
                                        data-media-path="media/video/WAT_09_03.mp4"
                                        data-caption-path="media/captions/WAT_09_03.vtt">Authentication Bypass</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_04.mp4"
                                        data-media-path="media/video/WAT_09_04.mp4"
                                        data-caption-path="media/captions/WAT_09_04.vtt">Enumerating the Database</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_05.mp4"
                                        data-media-path="media/video/WAT_09_05.mp4"
                                        data-caption-path="media/captions/WAT_09_05.vtt">Column Number Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_06.mp4"
                                        data-media-path="media/video/WAT_09_06.mp4"
                                        data-caption-path="media/captions/WAT_09_06.vtt">Understanding the Layout of the Output</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_07.mp4"
                                        data-media-path="media/video/WAT_09_07.mp4"
                                        data-caption-path="media/captions/WAT_09_07.vtt">Extracting Data from the Database</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_08.mp4"
                                        data-media-path="media/video/WAT_09_08.mp4"
                                        data-caption-path="media/captions/WAT_09_08.vtt">From SQL Injection to Code Execution</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_09_09.mp4"
                                        data-media-path="media/video/WAT_09_09.mp4"
                                        data-caption-path="media/captions/WAT_09_09.vtt">Automating SQL Injection</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WAT_10_00.mp4"
                                data-media-path="media/video/WAT_10_00.mp4"
                                data-caption-path="media/captions/WAT_10_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/BO_00_00.mp4"
                data-media-path="media/video/BO_00_00.mp4" data-caption-path="media/captions/BO_00_00.vtt">Introduction to Buffer Overflows</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_01_00.mp4"
                                data-media-path="media/video/BO_01_00.mp4"
                                data-caption-path="media/captions/BO_01_00.vtt">Introduction to the x86 Architecture</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_01_01.mp4"
                                        data-media-path="media/video/BO_01_01.mp4"
                                        data-caption-path="media/captions/BO_01_01.vtt">Program Memory</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_01_02.mp4"
                                        data-media-path="media/video/BO_01_02.mp4"
                                        data-caption-path="media/captions/BO_01_02.vtt">CPU Registers</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_02_00.mp4"
                                data-media-path="media/video/BO_02_00.mp4"
                                data-caption-path="media/captions/BO_02_00.vtt">Buffer Overflow Walkthrough</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_02_01.mp4"
                                        data-media-path="media/video/BO_02_01.mp4"
                                        data-caption-path="media/captions/BO_02_01.vtt">Sample Vulnerable Code</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_02_02.mp4"
                                        data-media-path="media/video/BO_02_02.mp4"
                                        data-caption-path="media/captions/BO_02_02.vtt">Introducing the Immunity Debugger</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_02_03.mp4"
                                        data-media-path="media/video/BO_02_03.mp4"
                                        data-caption-path="media/captions/BO_02_03.vtt">Navigating Code</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/BO_02_04.mp4"
                                        data-media-path="media/video/BO_02_04.mp4"
                                        data-caption-path="media/captions/BO_02_04.vtt">Overflowing the Buffer</a></li>
                </ul>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/WBO_00_00.mp4"
                data-media-path="media/video/WBO_00_00.mp4" data-caption-path="media/captions/WBO_00_00.vtt">Windows Buffer Overflows</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_01_00.mp4"
                                data-media-path="media/video/WBO_01_00.mp4"
                                data-caption-path="media/captions/WBO_01_00.vtt">Discovering the Vulnerability</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_01_01.mp4"
                                        data-media-path="media/video/WBO_01_01.mp4"
                                        data-caption-path="media/captions/WBO_01_01.vtt">Fuzzing the HTTP Protocol</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_00.mp4"
                                data-media-path="media/video/WBO_02_00.mp4"
                                data-caption-path="media/captions/WBO_02_00.vtt">Win32 Buffer Overflow Exploitation</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_01.mp4"
                                        data-media-path="media/video/WBO_02_01.mp4"
                                        data-caption-path="media/captions/WBO_02_01.vtt">Replicating the Crash</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_02.mp4"
                                        data-media-path="media/video/WBO_02_02.mp4"
                                        data-caption-path="media/captions/WBO_02_02.vtt">Controlling EIP</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_03.mp4"
                                        data-media-path="media/video/WBO_02_03.mp4"
                                        data-caption-path="media/captions/WBO_02_03.vtt">Locating Space for Our Shellcode</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_04.mp4"
                                        data-media-path="media/video/WBO_02_04.mp4"
                                        data-caption-path="media/captions/WBO_02_04.vtt">Checking for Bad Characters</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_05.mp4"
                                        data-media-path="media/video/WBO_02_05.mp4"
                                        data-caption-path="media/captions/WBO_02_05.vtt">Redirecting the Execution Flow</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_06.mp4"
                                        data-media-path="media/video/WBO_02_06.mp4"
                                        data-caption-path="media/captions/WBO_02_06.vtt">Finding a Return Address</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_07.mp4"
                                        data-media-path="media/video/WBO_02_07.mp4"
                                        data-caption-path="media/captions/WBO_02_07.vtt">Generating Shellcode with Metasploit</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_08.mp4"
                                        data-media-path="media/video/WBO_02_08.mp4"
                                        data-caption-path="media/captions/WBO_02_08.vtt">Getting a Shell</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_02_09.mp4"
                                        data-media-path="media/video/WBO_02_09.mp4"
                                        data-caption-path="media/captions/WBO_02_09.vtt">Improving the Exploit</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/WBO_03_00.mp4"
                                data-media-path="media/video/WBO_03_00.mp4"
                                data-caption-path="media/captions/WBO_03_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/LBO_00_00.mp4"
                data-media-path="media/video/LBO_00_00.mp4" data-caption-path="media/captions/LBO_00_00.vtt">Linux Buffer Overflows</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_01_00.mp4"
                                data-media-path="media/video/LBO_01_00.mp4"
                                data-caption-path="media/captions/LBO_01_00.vtt">About DEP, ASLR, and Canaries</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_02_00.mp4"
                                data-media-path="media/video/LBO_02_00.mp4"
                                data-caption-path="media/captions/LBO_02_00.vtt">Replicating the Crash</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_03_00.mp4"
                                data-media-path="media/video/LBO_03_00.mp4"
                                data-caption-path="media/captions/LBO_03_00.vtt">Controlling EIP</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_04_00.mp4"
                                data-media-path="media/video/LBO_04_00.mp4"
                                data-caption-path="media/captions/LBO_04_00.vtt">Locating Space for Our Shellcode</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_05_00.mp4"
                                data-media-path="media/video/LBO_05_00.mp4"
                                data-caption-path="media/captions/LBO_05_00.vtt">Checking for Bad Characters</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_06_00.mp4"
                                data-media-path="media/video/LBO_06_00.mp4"
                                data-caption-path="media/captions/LBO_06_00.vtt">Finding a Return Address</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_07_00.mp4"
                                data-media-path="media/video/LBO_07_00.mp4"
                                data-caption-path="media/captions/LBO_07_00.vtt">Getting a Shell</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LBO_08_00.mp4"
                                data-media-path="media/video/LBO_08_00.mp4"
                                data-caption-path="media/captions/LBO_08_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/CSA_00_00.mp4"
                data-media-path="media/video/CSA_00_00.mp4" data-caption-path="media/captions/CSA_00_00.vtt">Client-Side Attacks</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_01_00.mp4"
                                data-media-path="media/video/CSA_01_00.mp4"
                                data-caption-path="media/captions/CSA_01_00.vtt">Know Your Target</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_01_01.mp4"
                                        data-media-path="media/video/CSA_01_01.mp4"
                                        data-caption-path="media/captions/CSA_01_01.vtt">Passive Client Information Gathering</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_01_02.mp4"
                                        data-media-path="media/video/CSA_01_02.mp4"
                                        data-caption-path="media/captions/CSA_01_02.vtt">Active Client Information Gathering</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_01_03.mp4"
                                        data-media-path="media/video/CSA_01_03.mp4"
                                        data-caption-path="media/captions/CSA_01_03.vtt">Social Engineering and Client-Side Attacks</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_01_04.mp4"
                                        data-media-path="media/video/CSA_01_04.mp4"
                                        data-caption-path="media/captions/CSA_01_04.vtt">Client Fingerprinting</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_02_00.mp4"
                                data-media-path="media/video/CSA_02_00.mp4"
                                data-caption-path="media/captions/CSA_02_00.vtt">Leveraging HTML Applications</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_02_01.mp4"
                                        data-media-path="media/video/CSA_02_01.mp4"
                                        data-caption-path="media/captions/CSA_02_01.vtt">Exploring HTML Applications</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_02_02.mp4"
                                        data-media-path="media/video/CSA_02_02.mp4"
                                        data-caption-path="media/captions/CSA_02_02.vtt">HTA Attack in Action</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_03_00.mp4"
                                data-media-path="media/video/CSA_03_00.mp4"
                                data-caption-path="media/captions/CSA_03_00.vtt">Exploiting Microsoft Office</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_03_01.mp4"
                                        data-media-path="media/video/CSA_03_01.mp4"
                                        data-caption-path="media/captions/CSA_03_01.vtt">Microsoft Word Macro</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_03_02.mp4"
                                        data-media-path="media/video/CSA_03_02.mp4"
                                        data-caption-path="media/captions/CSA_03_02.vtt">Object Linking and Embedding</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_03_03.mp4"
                                        data-media-path="media/video/CSA_03_03.mp4"
                                        data-caption-path="media/captions/CSA_03_03.vtt">Evading Protected View</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/CSA_04_00.mp4"
                                data-media-path="media/video/CSA_04_00.mp4"
                                data-caption-path="media/captions/CSA_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/LPE_00_00.mp4"
                data-media-path="media/video/LPE_00_00.mp4" data-caption-path="media/captions/LPE_00_00.vtt">Locating Public Exploits</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_01_00.mp4"
                                data-media-path="media/video/LPE_01_00.mp4"
                                data-caption-path="media/captions/LPE_01_00.vtt">A Word of Caution</a>
                </li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_02_00.mp4"
                                data-media-path="media/video/LPE_02_00.mp4"
                                data-caption-path="media/captions/LPE_02_00.vtt">Searching for Exploits</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_02_01.mp4"
                                        data-media-path="media/video/LPE_02_01.mp4"
                                        data-caption-path="media/captions/LPE_02_01.vtt">Online Exploit Resources</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_02_02.mp4"
                                        data-media-path="media/video/LPE_02_02.mp4"
                                        data-caption-path="media/captions/LPE_02_02.vtt">Offline Exploit Resources</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_03_00.mp4"
                                data-media-path="media/video/LPE_03_00.mp4"
                                data-caption-path="media/captions/LPE_03_00.vtt">Putting It All Together</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/LPE_04_00.mp4"
                                data-media-path="media/video/LPE_04_00.mp4"
                                data-caption-path="media/captions/LPE_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/FE_00_00.mp4"
                data-media-path="media/video/FE_00_00.mp4" data-caption-path="media/captions/FE_00_00.vtt">Fixing Exploits</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_00.mp4"
                                data-media-path="media/video/FE_01_00.mp4"
                                data-caption-path="media/captions/FE_01_00.vtt">Fixing Memory Corruption Exploits</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_01.mp4"
                                        data-media-path="media/video/FE_01_01.mp4"
                                        data-caption-path="media/captions/FE_01_01.vtt">Examining the Exploit</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_02.mp4"
                                        data-media-path="media/video/FE_01_02.mp4"
                                        data-caption-path="media/captions/FE_01_02.vtt">Cross-Compiling The Exploit Code</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_03.mp4"
                                        data-media-path="media/video/FE_01_03.mp4"
                                        data-caption-path="media/captions/FE_01_03.vtt">Changing the Socket Information</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_04.mp4"
                                        data-media-path="media/video/FE_01_04.mp4"
                                        data-caption-path="media/captions/FE_01_04.vtt">Changing the Return Address</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_05.mp4"
                                        data-media-path="media/video/FE_01_05.mp4"
                                        data-caption-path="media/captions/FE_01_05.vtt">Changing the Payload</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_01_06.mp4"
                                        data-media-path="media/video/FE_01_06.mp4"
                                        data-caption-path="media/captions/FE_01_06.vtt">Changing the Overflow Buffer</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_02_00.mp4"
                                data-media-path="media/video/FE_02_00.mp4"
                                data-caption-path="media/captions/FE_02_00.vtt">Fixing Web Exploits</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_02_01.mp4"
                                        data-media-path="media/video/FE_02_01.mp4"
                                        data-caption-path="media/captions/FE_02_01.vtt">Considerations and Overview</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_02_02.mp4"
                                        data-media-path="media/video/FE_02_02.mp4"
                                        data-caption-path="media/captions/FE_02_02.vtt">Selecting the Vulnerability</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_02_03.mp4"
                                        data-media-path="media/video/FE_02_03.mp4"
                                        data-caption-path="media/captions/FE_02_03.vtt">Changing Connectivity Information</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_02_04.mp4"
                                        data-media-path="media/video/FE_02_04.mp4"
                                        data-caption-path="media/captions/FE_02_04.vtt">Troubleshooting the 'index out of range' Error</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FE_03_00.mp4"
                                data-media-path="media/video/FE_03_00.mp4"
                                data-caption-path="media/captions/FE_03_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/FT_00_00.mp4"
                data-media-path="media/video/FT_00_00.mp4" data-caption-path="media/captions/FT_00_00.vtt">File Transfers</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_01_00.mp4"
                                data-media-path="media/video/FT_01_00.mp4"
                                data-caption-path="media/captions/FT_01_00.vtt">Considerations and Preparations</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_01_01.mp4"
                                        data-media-path="media/video/FT_01_01.mp4"
                                        data-caption-path="media/captions/FT_01_01.vtt">Dangers of Transferring Attack Tools</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_01_02.mp4"
                                        data-media-path="media/video/FT_01_02.mp4"
                                        data-caption-path="media/captions/FT_01_02.vtt">Installing Pure-FTPd</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_01_03.mp4"
                                        data-media-path="media/video/FT_01_03.mp4"
                                        data-caption-path="media/captions/FT_01_03.vtt">The Non-Interactive Shell</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_00.mp4"
                                data-media-path="media/video/FT_02_00.mp4"
                                data-caption-path="media/captions/FT_02_00.vtt">Transferring Files with Windows Hosts</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_01.mp4"
                                        data-media-path="media/video/FT_02_01.mp4"
                                        data-caption-path="media/captions/FT_02_01.vtt">Non-Interactive FTP Download</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_02.mp4"
                                        data-media-path="media/video/FT_02_02.mp4"
                                        data-caption-path="media/captions/FT_02_02.vtt">Windows Downloads Using Scripting Languages</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_03.mp4"
                                        data-media-path="media/video/FT_02_03.mp4"
                                        data-caption-path="media/captions/FT_02_03.vtt">Windows Downloads with exe2hex and PowerShell</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_04.mp4"
                                        data-media-path="media/video/FT_02_04.mp4"
                                        data-caption-path="media/captions/FT_02_04.vtt">Windows Uploads Using Windows Scripting Languages</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_02_05.mp4"
                                        data-media-path="media/video/FT_02_05.mp4"
                                        data-caption-path="media/captions/FT_02_05.vtt">Uploading Files with TFTP</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/FT_03_00.mp4"
                                data-media-path="media/video/FT_03_00.mp4"
                                data-caption-path="media/captions/FT_03_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/AE_00_00.mp4"
                data-media-path="media/video/AE_00_00.mp4" data-caption-path="media/captions/AE_00_00.vtt">Antivirus Evasion</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_01_00.mp4"
                                data-media-path="media/video/AE_01_00.mp4"
                                data-caption-path="media/captions/AE_01_00.vtt">What is Antivirus Software</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_02_00.mp4"
                                data-media-path="media/video/AE_02_00.mp4"
                                data-caption-path="media/captions/AE_02_00.vtt">Methods of Detecting Malicious Code</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_02_01.mp4"
                                        data-media-path="media/video/AE_02_01.mp4"
                                        data-caption-path="media/captions/AE_02_01.vtt">Detection Methods</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_03_00.mp4"
                                data-media-path="media/video/AE_03_00.mp4"
                                data-caption-path="media/captions/AE_03_00.vtt">Bypassing Antivirus Detection</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_03_01.mp4"
                                        data-media-path="media/video/AE_03_01.mp4"
                                        data-caption-path="media/captions/AE_03_01.vtt">On-Disk Evasion</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_03_02.mp4"
                                        data-media-path="media/video/AE_03_02.mp4"
                                        data-caption-path="media/captions/AE_03_02.vtt">In-Memory Evasion</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_03_03.mp4"
                                        data-media-path="media/video/AE_03_03.mp4"
                                        data-caption-path="media/captions/AE_03_03.vtt">AV Evasion: Practical Example</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AE_04_00.mp4"
                                data-media-path="media/video/AE_04_00.mp4"
                                data-caption-path="media/captions/AE_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PX_00_00.mp4"
                data-media-path="media/video/PX_00_00.mp4" data-caption-path="media/captions/PX_00_00.vtt">Privilege Escalation</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_01_00.mp4"
                                data-media-path="media/video/PX_01_00.mp4"
                                data-caption-path="media/captions/PX_01_00.vtt">Information Gathering</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_01_01.mp4"
                                        data-media-path="media/video/PX_01_01.mp4"
                                        data-caption-path="media/captions/PX_01_01.vtt">Manual Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_01_02.mp4"
                                        data-media-path="media/video/PX_01_02.mp4"
                                        data-caption-path="media/captions/PX_01_02.vtt">Automated Enumeration</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_00.mp4"
                                data-media-path="media/video/PX_02_00.mp4"
                                data-caption-path="media/captions/PX_02_00.vtt">Windows Privilege Escalation Examples</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_01.mp4"
                                        data-media-path="media/video/PX_02_01.mp4"
                                        data-caption-path="media/captions/PX_02_01.vtt">Understanding Windows Privileges and Integrity Levels</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_02.mp4"
                                        data-media-path="media/video/PX_02_02.mp4"
                                        data-caption-path="media/captions/PX_02_02.vtt">Introduction to User Account Control (UAC)</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_03.mp4"
                                        data-media-path="media/video/PX_02_03.mp4"
                                        data-caption-path="media/captions/PX_02_03.vtt">User Account Control Bypass: Case Study</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_04.mp4"
                                        data-media-path="media/video/PX_02_04.mp4"
                                        data-caption-path="media/captions/PX_02_04.vtt">Insecure File Permissions: Serviio Case Study</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_05.mp4"
                                        data-media-path="media/video/PX_02_05.mp4"
                                        data-caption-path="media/captions/PX_02_05.vtt">Leveraging Unquoted Service Paths</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_02_06.mp4"
                                        data-media-path="media/video/PX_02_06.mp4"
                                        data-caption-path="media/captions/PX_02_06.vtt">Windows Kernel Vulnerabilities: USBPcap Case Study</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_03_00.mp4"
                                data-media-path="media/video/PX_03_00.mp4"
                                data-caption-path="media/captions/PX_03_00.vtt">Linux Privilege Escalation Examples</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_03_01.mp4"
                                        data-media-path="media/video/PX_03_01.mp4"
                                        data-caption-path="media/captions/PX_03_01.vtt">Understanding Linux Privileges</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_03_02.mp4"
                                        data-media-path="media/video/PX_03_02.mp4"
                                        data-caption-path="media/captions/PX_03_02.vtt">Insecure File Permissions: Cron Case Study</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_03_03.mp4"
                                        data-media-path="media/video/PX_03_03.mp4"
                                        data-caption-path="media/captions/PX_03_03.vtt">Insecure File Permissions: /etc/passwd Case Study</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_03_04.mp4"
                                        data-media-path="media/video/PX_03_04.mp4"
                                        data-caption-path="media/captions/PX_03_04.vtt">Linux Kernel Vulnerabilities: Case Study</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PX_04_00.mp4"
                                data-media-path="media/video/PX_04_00.mp4"
                                data-caption-path="media/captions/PX_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PA_00_00.mp4"
                data-media-path="media/video/PA_00_00.mp4" data-caption-path="media/captions/PA_00_00.vtt">Password Attacks</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_01_00.mp4"
                                data-media-path="media/video/PA_01_00.mp4"
                                data-caption-path="media/captions/PA_01_00.vtt">Wordlists</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_01_01.mp4"
                                        data-media-path="media/video/PA_01_01.mp4"
                                        data-caption-path="media/captions/PA_01_01.vtt">Standard Wordlists</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_02_00.mp4"
                                data-media-path="media/video/PA_02_00.mp4"
                                data-caption-path="media/captions/PA_02_00.vtt">Brute Force Wordlists</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_03_00.mp4"
                                data-media-path="media/video/PA_03_00.mp4"
                                data-caption-path="media/captions/PA_03_00.vtt">Common Network Service Attack Methods</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_03_01.mp4"
                                        data-media-path="media/video/PA_03_01.mp4"
                                        data-caption-path="media/captions/PA_03_01.vtt">HTTP htaccess Attack with Medusa</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_03_02.mp4"
                                        data-media-path="media/video/PA_03_02.mp4"
                                        data-caption-path="media/captions/PA_03_02.vtt">Remote Desktop Protocol Attack with Crowbar</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_03_03.mp4"
                                        data-media-path="media/video/PA_03_03.mp4"
                                        data-caption-path="media/captions/PA_03_03.vtt">SSH Attack with THC-Hydra</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_03_04.mp4"
                                        data-media-path="media/video/PA_03_04.mp4"
                                        data-caption-path="media/captions/PA_03_04.vtt">HTTP POST Attack with THC-Hydra</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_04_00.mp4"
                                data-media-path="media/video/PA_04_00.mp4"
                                data-caption-path="media/captions/PA_04_00.vtt">Leveraging Password Hashes</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_04_01.mp4"
                                        data-media-path="media/video/PA_04_01.mp4"
                                        data-caption-path="media/captions/PA_04_01.vtt">Retrieving Password Hashes</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_04_02.mp4"
                                        data-media-path="media/video/PA_04_02.mp4"
                                        data-caption-path="media/captions/PA_04_02.vtt">Passing the Hash in Windows</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_04_03.mp4"
                                        data-media-path="media/video/PA_04_03.mp4"
                                        data-caption-path="media/captions/PA_04_03.vtt">Password Cracking</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PA_05_00.mp4"
                                data-media-path="media/video/PA_05_00.mp4"
                                data-caption-path="media/captions/PA_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PRT_00_00.mp4"
                data-media-path="media/video/PRT_00_00.mp4" data-caption-path="media/captions/PRT_00_00.vtt">Port Redirection and Tunneling</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_01_00.mp4"
                                data-media-path="media/video/PRT_01_00.mp4"
                                data-caption-path="media/captions/PRT_01_00.vtt">Port Forwarding</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_01_01.mp4"
                                        data-media-path="media/video/PRT_01_01.mp4"
                                        data-caption-path="media/captions/PRT_01_01.vtt">RINETD</a>
                        </li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_02_00.mp4"
                                data-media-path="media/video/PRT_02_00.mp4"
                                data-caption-path="media/captions/PRT_02_00.vtt">SSH Tunneling</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_02_01.mp4"
                                        data-media-path="media/video/PRT_02_01.mp4"
                                        data-caption-path="media/captions/PRT_02_01.vtt">SSH Local Port Forwarding</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_02_02.mp4"
                                        data-media-path="media/video/PRT_02_02.mp4"
                                        data-caption-path="media/captions/PRT_02_02.vtt">SSH Remote Port Forwarding</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_02_03.mp4"
                                        data-media-path="media/video/PRT_02_03.mp4"
                                        data-caption-path="media/captions/PRT_02_03.vtt">SSH Dynamic Port Forwarding</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_03_00.mp4"
                                data-media-path="media/video/PRT_03_00.mp4"
                                data-caption-path="media/captions/PRT_03_00.vtt">PLINK.exe</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_04_00.mp4"
                                data-media-path="media/video/PRT_04_00.mp4"
                                data-caption-path="media/captions/PRT_04_00.vtt">NETSH</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_05_00.mp4"
                                data-media-path="media/video/PRT_05_00.mp4"
                                data-caption-path="media/captions/PRT_05_00.vtt">HTTPTunnel-ing Through Deep Packet Inspection</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PRT_06_00.mp4"
                                data-media-path="media/video/PRT_06_00.mp4"
                                data-caption-path="media/captions/PRT_06_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/AD_00_00.mp4"
                data-media-path="media/video/AD_00_00.mp4" data-caption-path="media/captions/AD_00_00.vtt">Active Directory Attacks</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_01_00.mp4"
                                data-media-path="media/video/AD_01_00.mp4"
                                data-caption-path="media/captions/AD_01_00.vtt">Active Directory Theory</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_00.mp4"
                                data-media-path="media/video/AD_02_00.mp4"
                                data-caption-path="media/captions/AD_02_00.vtt">Active Directory Enumeration</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_01.mp4"
                                        data-media-path="media/video/AD_02_01.mp4"
                                        data-caption-path="media/captions/AD_02_01.vtt">Traditional Approach</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_02.mp4"
                                        data-media-path="media/video/AD_02_02.mp4"
                                        data-caption-path="media/captions/AD_02_02.vtt">A Modern Approach</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_03.mp4"
                                        data-media-path="media/video/AD_02_03.mp4"
                                        data-caption-path="media/captions/AD_02_03.vtt">Resolving Nested Groups</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_04.mp4"
                                        data-media-path="media/video/AD_02_04.mp4"
                                        data-caption-path="media/captions/AD_02_04.vtt">Currently Logged on Users</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_02_05.mp4"
                                        data-media-path="media/video/AD_02_05.mp4"
                                        data-caption-path="media/captions/AD_02_05.vtt">Enumeration Through Service Principal Names</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_00.mp4"
                                data-media-path="media/video/AD_03_00.mp4"
                                data-caption-path="media/captions/AD_03_00.vtt">Active Directory Authentication</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_01.mp4"
                                        data-media-path="media/video/AD_03_01.mp4"
                                        data-caption-path="media/captions/AD_03_01.vtt">NTLM Authentication</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_02.mp4"
                                        data-media-path="media/video/AD_03_02.mp4"
                                        data-caption-path="media/captions/AD_03_02.vtt">Kerberos Authentication</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_03.mp4"
                                        data-media-path="media/video/AD_03_03.mp4"
                                        data-caption-path="media/captions/AD_03_03.vtt">Cached Credential Storage and Retrieval</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_04.mp4"
                                        data-media-path="media/video/AD_03_04.mp4"
                                        data-caption-path="media/captions/AD_03_04.vtt">Service Account Attacks</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_03_05.mp4"
                                        data-media-path="media/video/AD_03_05.mp4"
                                        data-caption-path="media/captions/AD_03_05.vtt">Low and Slow Password Guessing</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_04_00.mp4"
                                data-media-path="media/video/AD_04_00.mp4"
                                data-caption-path="media/captions/AD_04_00.vtt">Active Directory Lateral Movement</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_04_01.mp4"
                                        data-media-path="media/video/AD_04_01.mp4"
                                        data-caption-path="media/captions/AD_04_01.vtt">Pass the Hash</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_04_02.mp4"
                                        data-media-path="media/video/AD_04_02.mp4"
                                        data-caption-path="media/captions/AD_04_02.vtt">Overpass the Hash</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_04_03.mp4"
                                        data-media-path="media/video/AD_04_03.mp4"
                                        data-caption-path="media/captions/AD_04_03.vtt">Pass the Ticket</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_04_04.mp4"
                                        data-media-path="media/video/AD_04_04.mp4"
                                        data-caption-path="media/captions/AD_04_04.vtt">Distributed Component Object Model</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_05_00.mp4"
                                data-media-path="media/video/AD_05_00.mp4"
                                data-caption-path="media/captions/AD_05_00.vtt">Active Directory Persistence</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_05_01.mp4"
                                        data-media-path="media/video/AD_05_01.mp4"
                                        data-caption-path="media/captions/AD_05_01.vtt">Golden Tickets</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_05_02.mp4"
                                        data-media-path="media/video/AD_05_02.mp4"
                                        data-caption-path="media/captions/AD_05_02.vtt">Domain Controller Synchronization</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/AD_06_00.mp4"
                                data-media-path="media/video/AD_06_00.mp4"
                                data-caption-path="media/captions/AD_06_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/MF_00_00.mp4"
                data-media-path="media/video/MF_00_00.mp4" data-caption-path="media/captions/MF_00_00.vtt">The Metasploit Framework</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_01_00.mp4"
                                data-media-path="media/video/MF_01_00.mp4"
                                data-caption-path="media/captions/MF_01_00.vtt">Metasploit User Interfaces and Setup</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_01_01.mp4"
                                        data-media-path="media/video/MF_01_01.mp4"
                                        data-caption-path="media/captions/MF_01_01.vtt">Getting Familiar with MSF Syntax</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_01_02.mp4"
                                        data-media-path="media/video/MF_01_02.mp4"
                                        data-caption-path="media/captions/MF_01_02.vtt">Metasploit Database Access</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_01_03.mp4"
                                        data-media-path="media/video/MF_01_03.mp4"
                                        data-caption-path="media/captions/MF_01_03.vtt">Auxiliary Modules</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_02_00.mp4"
                                data-media-path="media/video/MF_02_00.mp4"
                                data-caption-path="media/captions/MF_02_00.vtt">Exploit Modules</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_00.mp4"
                                data-media-path="media/video/MF_03_00.mp4"
                                data-caption-path="media/captions/MF_03_00.vtt">Metasploit Payloads</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_01.mp4"
                                        data-media-path="media/video/MF_03_01.mp4"
                                        data-caption-path="media/captions/MF_03_01.vtt">Staged vs Non-Staged Payloads</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_02.mp4"
                                        data-media-path="media/video/MF_03_02.mp4"
                                        data-caption-path="media/captions/MF_03_02.vtt">Meterpreter Payloads</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_03.mp4"
                                        data-media-path="media/video/MF_03_03.mp4"
                                        data-caption-path="media/captions/MF_03_03.vtt">Experimenting with Meterpreter</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_04.mp4"
                                        data-media-path="media/video/MF_03_04.mp4"
                                        data-caption-path="media/captions/MF_03_04.vtt">Executable Payloads</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_05.mp4"
                                        data-media-path="media/video/MF_03_05.mp4"
                                        data-caption-path="media/captions/MF_03_05.vtt">Metasploit Exploit Multi Handler</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_06.mp4"
                                        data-media-path="media/video/MF_03_06.mp4"
                                        data-caption-path="media/captions/MF_03_06.vtt">Client-Side Attacks</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_03_07.mp4"
                                        data-media-path="media/video/MF_03_07.mp4"
                                        data-caption-path="media/captions/MF_03_07.vtt">Advanced Features and Transports</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_04_00.mp4"
                                data-media-path="media/video/MF_04_00.mp4"
                                data-caption-path="media/captions/MF_04_00.vtt">Building Our Own MSF Module</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_05_00.mp4"
                                data-media-path="media/video/MF_05_00.mp4"
                                data-caption-path="media/captions/MF_05_00.vtt">Post-Exploitation with Metasploit</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_05_01.mp4"
                                        data-media-path="media/video/MF_05_01.mp4"
                                        data-caption-path="media/captions/MF_05_01.vtt">Core Post-Exploitation Features</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_05_02.mp4"
                                        data-media-path="media/video/MF_05_02.mp4"
                                        data-caption-path="media/captions/MF_05_02.vtt">Migrating Processes</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_05_03.mp4"
                                        data-media-path="media/video/MF_05_03.mp4"
                                        data-caption-path="media/captions/MF_05_03.vtt">Post-Exploitation Modules</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_05_04.mp4"
                                        data-media-path="media/video/MF_05_04.mp4"
                                        data-caption-path="media/captions/MF_05_04.vtt">Pivoting with the Metasploit Framework</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_06_00.mp4"
                                data-media-path="media/video/MF_06_00.mp4"
                                data-caption-path="media/captions/MF_06_00.vtt">Metasploit Automation</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/MF_07_00.mp4"
                                data-media-path="media/video/MF_07_00.mp4"
                                data-caption-path="media/captions/MF_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/PE_00_00.mp4"
                data-media-path="media/video/PE_00_00.mp4" data-caption-path="media/captions/PE_00_00.vtt">PowerShell Empire</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_01_00.mp4"
                                data-media-path="media/video/PE_01_00.mp4"
                                data-caption-path="media/captions/PE_01_00.vtt">Installation, Setup, and Usage</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_01_01.mp4"
                                        data-media-path="media/video/PE_01_01.mp4"
                                        data-caption-path="media/captions/PE_01_01.vtt">PowerShell Empire Syntax</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_01_02.mp4"
                                        data-media-path="media/video/PE_01_02.mp4"
                                        data-caption-path="media/captions/PE_01_02.vtt">Listeners and Stagers</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_01_03.mp4"
                                        data-media-path="media/video/PE_01_03.mp4"
                                        data-caption-path="media/captions/PE_01_03.vtt">The Empire Agent</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_02_00.mp4"
                                data-media-path="media/video/PE_02_00.mp4"
                                data-caption-path="media/captions/PE_02_00.vtt">PowerShell Modules</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_02_01.mp4"
                                        data-media-path="media/video/PE_02_01.mp4"
                                        data-caption-path="media/captions/PE_02_01.vtt">Situational Awareness</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_02_02.mp4"
                                        data-media-path="media/video/PE_02_02.mp4"
                                        data-caption-path="media/captions/PE_02_02.vtt">Credentials and Privilege Escalation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_02_03.mp4"
                                        data-media-path="media/video/PE_02_03.mp4"
                                        data-caption-path="media/captions/PE_02_03.vtt">Lateral Movement</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_03_00.mp4"
                                data-media-path="media/video/PE_03_00.mp4"
                                data-caption-path="media/captions/PE_03_00.vtt">Switching Between Empire and Metasploit</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/PE_04_00.mp4"
                                data-media-path="media/video/PE_04_00.mp4"
                                data-caption-path="media/captions/PE_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module" href="https://pwk.hide01.ir/media/video/ATP_00_00.mp4"
                data-media-path="media/video/ATP_00_00.mp4" data-caption-path="media/captions/ATP_00_00.vtt">Assembling the Pieces: Penetration Test Breakdown</a>
        <ul class="submenu">
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_01_00.mp4"
                                data-media-path="media/video/ATP_01_00.mp4"
                                data-caption-path="media/captions/ATP_01_00.vtt">Public Network Enumeration</a></li>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_00.mp4"
                                data-media-path="media/video/ATP_02_00.mp4"
                                data-caption-path="media/captions/ATP_02_00.vtt">Targeting the Web Application</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_01.mp4"
                                        data-media-path="media/video/ATP_02_01.mp4"
                                        data-caption-path="media/captions/ATP_02_01.vtt">Web Application Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_02.mp4"
                                        data-media-path="media/video/ATP_02_02.mp4"
                                        data-caption-path="media/captions/ATP_02_02.vtt">SQL Injection Exploitation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_03.mp4"
                                        data-media-path="media/video/ATP_02_03.mp4"
                                        data-caption-path="media/captions/ATP_02_03.vtt">Cracking the Password</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_04.mp4"
                                        data-media-path="media/video/ATP_02_04.mp4"
                                        data-caption-path="media/captions/ATP_02_04.vtt">Enumerating the Admin Interface</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_05.mp4"
                                        data-media-path="media/video/ATP_02_05.mp4"
                                        data-caption-path="media/captions/ATP_02_05.vtt">Obtaining a Shell</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_06.mp4"
                                        data-media-path="media/video/ATP_02_06.mp4"
                                        data-caption-path="media/captions/ATP_02_06.vtt">Post-Exploitation Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_02_07.mp4"
                                        data-media-path="media/video/ATP_02_07.mp4"
                                        data-caption-path="media/captions/ATP_02_07.vtt">Creating a Stable Pivot Point</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_03_00.mp4"
                                data-media-path="media/video/ATP_03_00.mp4"
                                data-caption-path="media/captions/ATP_03_00.vtt">Targeting the Database</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_03_01.mp4"
                                        data-media-path="media/video/ATP_03_01.mp4"
                                        data-caption-path="media/captions/ATP_03_01.vtt">Enumeration</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_03_02.mp4"
                                        data-media-path="media/video/ATP_03_02.mp4"
                                        data-caption-path="media/captions/ATP_03_02.vtt">Attempting to Exploit the Database</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_04_00.mp4"
                                data-media-path="media/video/ATP_04_00.mp4"
                                data-caption-path="media/captions/ATP_04_00.vtt">Deeper Enumeration of the Web Application Server</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_04_01.mp4"
                                        data-media-path="media/video/ATP_04_01.mp4"
                                        data-caption-path="media/captions/ATP_04_01.vtt">More Thorough Post Exploitation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_04_02.mp4"
                                        data-media-path="media/video/ATP_04_02.mp4"
                                        data-caption-path="media/captions/ATP_04_02.vtt">Privilege Escalation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_04_03.mp4"
                                        data-media-path="media/video/ATP_04_03.mp4"
                                        data-caption-path="media/captions/ATP_04_03.vtt">Searching for DB Credentials</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_05_00.mp4"
                                data-media-path="media/video/ATP_05_00.mp4"
                                data-caption-path="media/captions/ATP_05_00.vtt">Targeting the Database Again</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_05_01.mp4"
                                        data-media-path="media/video/ATP_05_01.mp4"
                                        data-caption-path="media/captions/ATP_05_01.vtt">Exploitation</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_05_02.mp4"
                                        data-media-path="media/video/ATP_05_02.mp4"
                                        data-caption-path="media/captions/ATP_05_02.vtt">Post-Exploitation Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_05_03.mp4"
                                        data-media-path="media/video/ATP_05_03.mp4"
                                        data-caption-path="media/captions/ATP_05_03.vtt">Creating a Stable Reverse Tunnel</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_00.mp4"
                                data-media-path="media/video/ATP_06_00.mp4"
                                data-caption-path="media/captions/ATP_06_00.vtt">Targeting Poultry</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_01.mp4"
                                        data-media-path="media/video/ATP_06_01.mp4"
                                        data-caption-path="media/captions/ATP_06_01.vtt">Enumeration</a>
                        </li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_02.mp4"
                                        data-media-path="media/video/ATP_06_02.mp4"
                                        data-caption-path="media/captions/ATP_06_02.vtt">Exploitation (Or Just Logging In)</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_03.mp4"
                                        data-media-path="media/video/ATP_06_03.mp4"
                                        data-caption-path="media/captions/ATP_06_03.vtt">Post-Exploitation Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_04.mp4"
                                        data-media-path="media/video/ATP_06_04.mp4"
                                        data-caption-path="media/captions/ATP_06_04.vtt">Unquoted Search Path Exploitation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_06_05.mp4"
                                        data-media-path="media/video/ATP_06_05.mp4"
                                        data-caption-path="media/captions/ATP_06_05.vtt">Post-Exploitation Enumeration</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_07_00.mp4"
                                data-media-path="media/video/ATP_07_00.mp4"
                                data-caption-path="media/captions/ATP_07_00.vtt">Internal Network Enumeration</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_07_01.mp4"
                                        data-media-path="media/video/ATP_07_01.mp4"
                                        data-caption-path="media/captions/ATP_07_01.vtt">Reviewing the Results</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_00.mp4"
                                data-media-path="media/video/ATP_08_00.mp4"
                                data-caption-path="media/captions/ATP_08_00.vtt">Targeting the Jenkins Server</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_01.mp4"
                                        data-media-path="media/video/ATP_08_01.mp4"
                                        data-caption-path="media/captions/ATP_08_01.vtt">Application Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_02.mp4"
                                        data-media-path="media/video/ATP_08_02.mp4"
                                        data-caption-path="media/captions/ATP_08_02.vtt">Exploiting Jenkins</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_03.mp4"
                                        data-media-path="media/video/ATP_08_03.mp4"
                                        data-caption-path="media/captions/ATP_08_03.vtt">Post Exploitation Enumeration</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_04.mp4"
                                        data-media-path="media/video/ATP_08_04.mp4"
                                        data-caption-path="media/captions/ATP_08_04.vtt">Privilege Escalation</a></li>
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_08_05.mp4"
                                        data-media-path="media/video/ATP_08_05.mp4"
                                        data-caption-path="media/captions/ATP_08_05.vtt">Post Exploitation Enumeration</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_09_00.mp4"
                                data-media-path="media/video/ATP_09_00.mp4"
                                data-caption-path="media/captions/ATP_09_00.vtt">Targeting the Domain Controller</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_09_01.mp4"
                                        data-media-path="media/video/ATP_09_01.mp4"
                                        data-caption-path="media/captions/ATP_09_01.vtt">Exploiting the Domain Controller</a></li>
                </ul>
                <li><a class="sub-module" href="https://pwk.hide01.ir/media/video/ATP_10_00.mp4"
                                data-media-path="media/video/ATP_10_00.mp4"
                                data-caption-path="media/captions/ATP_10_00.vtt">Wrapping Up</a></li>
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
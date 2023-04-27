import urllib.request
import os
from bs4 import BeautifulSoup
import json

html_code = """
<li class="module-title open"><a class="module active"
                href="https://xyz.website/media/video/TM_00_00.mp4"
                data-media-path="media/video/TM_00_00.mp4" data-caption-path="media/captions/TM_00_00.vtt">Tools &amp;
                Methodologies</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_01_00.mp4"
                                data-media-path="media/video/TM_01_00.mp4"
                                data-caption-path="media/captions/TM_01_00.vtt">Web Traffic Inspection</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_01_01.mp4"
                                        data-media-path="media/video/TM_01_01.mp4"
                                        data-caption-path="media/captions/TM_01_01.vtt">BurpSuite Proxy</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_01_02.mp4"
                                        data-media-path="media/video/TM_01_02.mp4"
                                        data-caption-path="media/captions/TM_01_02.vtt">Using Burp Suite with Other Browsers</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_01_03.mp4"
                                        data-media-path="media/video/TM_01_03.mp4"
                                        data-caption-path="media/captions/TM_01_03.vtt">Burp Suite Scope</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_01_04.mp4"
                                        data-media-path="media/video/TM_01_04.mp4"
                                        data-caption-path="media/captions/TM_01_04.vtt">Burp Suite Repeater and Comparer</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_01_05.mp4"
                                        data-media-path="media/video/TM_01_05.mp4"
                                        data-caption-path="media/captions/TM_01_05.vtt">Burp Suite Decoder</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_02_00.mp4"
                                data-media-path="media/video/TM_02_00.mp4"
                                data-caption-path="media/captions/TM_02_00.vtt">Interacting with Web Listeners using Python</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_03_00.mp4"
                                data-media-path="media/video/TM_03_00.mp4"
                                data-caption-path="media/captions/TM_03_00.vtt">Source Code Recovery</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_03_01.mp4"
                                        data-media-path="media/video/TM_03_01.mp4"
                                        data-caption-path="media/captions/TM_03_01.vtt">Managed .NET Code</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_03_02.mp4"
                                        data-media-path="media/video/TM_03_02.mp4"
                                        data-caption-path="media/captions/TM_03_02.vtt">Decompiling Java Classes</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_04_00.mp4"
                                data-media-path="media/video/TM_04_00.mp4"
                                data-caption-path="media/captions/TM_04_00.vtt">Source Code Analysis Methodology</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_04_01.mp4"
                                        data-media-path="media/video/TM_04_01.mp4"
                                        data-caption-path="media/captions/TM_04_01.vtt">An Approach to Analysis</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_04_02.mp4"
                                        data-media-path="media/video/TM_04_02.mp4"
                                        data-caption-path="media/captions/TM_04_02.vtt">Using an IDE</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_04_03.mp4"
                                        data-media-path="media/video/TM_04_03.mp4"
                                        data-caption-path="media/captions/TM_04_03.vtt">Common HTTP Routing Patterns</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_04_04.mp4"
                                        data-media-path="media/video/TM_04_04.mp4"
                                        data-caption-path="media/captions/TM_04_04.vtt">Analyzing Source Code for Vulnerabilities</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_05_00.mp4"
                                data-media-path="media/video/TM_05_00.mp4"
                                data-caption-path="media/captions/TM_05_00.vtt">Debugging</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/TM_05_01.mp4"
                                        data-media-path="media/video/TM_05_01.mp4"
                                        data-caption-path="media/captions/TM_05_01.vtt">Remote Debugging</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/TM_06_00.mp4"
                                data-media-path="media/video/TM_06_00.mp4"
                                data-caption-path="media/captions/TM_06_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/AAB_00_00.mp4"
                data-media-path="media/video/AAB_00_00.mp4" data-caption-path="media/captions/AAB_00_00.vtt">ATutor Authentication Bypass and RCE</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_01_00.mp4"
                                data-media-path="media/video/AAB_01_00.mp4"
                                data-caption-path="media/captions/AAB_01_00.vtt">Getting Started</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_01_01.mp4"
                                        data-media-path="media/video/AAB_01_01.mp4"
                                        data-caption-path="media/captions/AAB_01_01.vtt">Setting Up the Environment</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_02_00.mp4"
                                data-media-path="media/video/AAB_02_00.mp4"
                                data-caption-path="media/captions/AAB_02_00.vtt">Initial Vulnerability Discovery</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_03_00.mp4"
                                data-media-path="media/video/AAB_03_00.mp4"
                                data-caption-path="media/captions/AAB_03_00.vtt">A Brief Review of Blind SQL Injections</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_04_00.mp4"
                                data-media-path="media/video/AAB_04_00.mp4"
                                data-caption-path="media/captions/AAB_04_00.vtt">Digging Deeper</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_04_01.mp4"
                                        data-media-path="media/video/AAB_04_01.mp4"
                                        data-caption-path="media/captions/AAB_04_01.vtt">When $addslashes Are Not</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_04_02.mp4"
                                        data-media-path="media/video/AAB_04_02.mp4"
                                        data-caption-path="media/captions/AAB_04_02.vtt">Improper Use of Parameterization</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_05_00.mp4"
                                data-media-path="media/video/AAB_05_00.mp4"
                                data-caption-path="media/captions/AAB_05_00.vtt">Data Exfiltration</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_05_01.mp4"
                                        data-media-path="media/video/AAB_05_01.mp4"
                                        data-caption-path="media/captions/AAB_05_01.vtt">Comparing HTML Responses</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_05_02.mp4"
                                        data-media-path="media/video/AAB_05_02.mp4"
                                        data-caption-path="media/captions/AAB_05_02.vtt">MySQL Version Extraction</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_06_00.mp4"
                                data-media-path="media/video/AAB_06_00.mp4"
                                data-caption-path="media/captions/AAB_06_00.vtt">Subverting the ATutor Authentication</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_07_00.mp4"
                                data-media-path="media/video/AAB_07_00.mp4"
                                data-caption-path="media/captions/AAB_07_00.vtt">Authentication Gone Bad</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_08_00.mp4"
                                data-media-path="media/video/AAB_08_00.mp4"
                                data-caption-path="media/captions/AAB_08_00.vtt">Bypassing File Upload Restrictions</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_09_00.mp4"
                                data-media-path="media/video/AAB_09_00.mp4"
                                data-caption-path="media/captions/AAB_09_00.vtt">Gaining Remote Code Execution</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_09_01.mp4"
                                        data-media-path="media/video/AAB_09_01.mp4"
                                        data-caption-path="media/captions/AAB_09_01.vtt">Escaping the Jail</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_09_02.mp4"
                                        data-media-path="media/video/AAB_09_02.mp4"
                                        data-caption-path="media/captions/AAB_09_02.vtt">Disclosing the Web Root</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_09_03.mp4"
                                        data-media-path="media/video/AAB_09_03.mp4"
                                        data-caption-path="media/captions/AAB_09_03.vtt">Finding Writable Directories</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/AAB_09_04.mp4"
                                        data-media-path="media/video/AAB_09_04.mp4"
                                        data-caption-path="media/captions/AAB_09_04.vtt">Bypassing File Extension Filter</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/AAB_10_00.mp4"
                                data-media-path="media/video/AAB_10_00.mp4"
                                data-caption-path="media/captions/AAB_10_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/ATJ_00_00.mp4"
                data-media-path="media/video/ATJ_00_00.mp4" data-caption-path="media/captions/ATJ_00_00.vtt">ATutor LMS Type Juggling Vulnerability</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_01_00.mp4"
                                data-media-path="media/video/ATJ_01_00.mp4"
                                data-caption-path="media/captions/ATJ_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_02_00.mp4"
                                data-media-path="media/video/ATJ_02_00.mp4"
                                data-caption-path="media/captions/ATJ_02_00.vtt">PHP Loose and Strict Comparisons</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_03_00.mp4"
                                data-media-path="media/video/ATJ_03_00.mp4"
                                data-caption-path="media/captions/ATJ_03_00.vtt">PHP String Conversion to Numbers</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_04_00.mp4"
                                data-media-path="media/video/ATJ_04_00.mp4"
                                data-caption-path="media/captions/ATJ_04_00.vtt">Vulnerability Discovery</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_05_00.mp4"
                                data-media-path="media/video/ATJ_05_00.mp4"
                                data-caption-path="media/captions/ATJ_05_00.vtt">Attacking the Loose Comparison</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ATJ_05_01.mp4"
                                        data-media-path="media/video/ATJ_05_01.mp4"
                                        data-caption-path="media/captions/ATJ_05_01.vtt">Magic Hashes</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ATJ_05_02.mp4"
                                        data-media-path="media/video/ATJ_05_02.mp4"
                                        data-caption-path="media/captions/ATJ_05_02.vtt">ATutor and the Magic E-Mail address</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ATJ_06_00.mp4"
                                data-media-path="media/video/ATJ_06_00.mp4"
                                data-caption-path="media/captions/ATJ_06_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/MSI_00_00.mp4"
                data-media-path="media/video/MSI_00_00.mp4"
                data-caption-path="media/captions/MSI_00_00.vtt">ManageEngine Applications Manager AMUserResourcesSyncServlet SQL Injection RCE</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_01_00.mp4"
                                data-media-path="media/video/MSI_01_00.mp4"
                                data-caption-path="media/captions/MSI_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_02_00.mp4"
                                data-media-path="media/video/MSI_02_00.mp4"
                                data-caption-path="media/captions/MSI_02_00.vtt">Vulnerability Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_02_01.mp4"
                                        data-media-path="media/video/MSI_02_01.mp4"
                                        data-caption-path="media/captions/MSI_02_01.vtt">Servlet Mappings</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_02_02.mp4"
                                        data-media-path="media/video/MSI_02_02.mp4"
                                        data-caption-path="media/captions/MSI_02_02.vtt">Source Code Recovery</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_02_03.mp4"
                                        data-media-path="media/video/MSI_02_03.mp4"
                                        data-caption-path="media/captions/MSI_02_03.vtt">Analyzing the Source Code</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_02_04.mp4"
                                        data-media-path="media/video/MSI_02_04.mp4"
                                        data-caption-path="media/captions/MSI_02_04.vtt">Enabling Database Logging</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_02_05.mp4"
                                        data-media-path="media/video/MSI_02_05.mp4"
                                        data-caption-path="media/captions/MSI_02_05.vtt">Triggering the Vulnerability</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_03_00.mp4"
                                data-media-path="media/video/MSI_03_00.mp4"
                                data-caption-path="media/captions/MSI_03_00.vtt">How Houdini Escapes</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_03_01.mp4"
                                        data-media-path="media/video/MSI_03_01.mp4"
                                        data-caption-path="media/captions/MSI_03_01.vtt">Using CHR and String Concatenation</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_03_02.mp4"
                                        data-media-path="media/video/MSI_03_02.mp4"
                                        data-caption-path="media/captions/MSI_03_02.vtt">It Makes Lexical Sense</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_04_00.mp4"
                                data-media-path="media/video/MSI_04_00.mp4"
                                data-caption-path="media/captions/MSI_04_00.vtt">Blind Bats</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_05_00.mp4"
                                data-media-path="media/video/MSI_05_00.mp4"
                                data-caption-path="media/captions/MSI_05_00.vtt">Accessing the File System</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_05_01.mp4"
                                        data-media-path="media/video/MSI_05_01.mp4"
                                        data-caption-path="media/captions/MSI_05_01.vtt">Reverse Shell via Copy To</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_06_00.mp4"
                                data-media-path="media/video/MSI_06_00.mp4"
                                data-caption-path="media/captions/MSI_06_00.vtt">PostgreSQL Extensions</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_06_01.mp4"
                                        data-media-path="media/video/MSI_06_01.mp4"
                                        data-caption-path="media/captions/MSI_06_01.vtt">Build Environment</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_06_02.mp4"
                                        data-media-path="media/video/MSI_06_02.mp4"
                                        data-caption-path="media/captions/MSI_06_02.vtt">Testing the Extension</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_06_03.mp4"
                                        data-media-path="media/video/MSI_06_03.mp4"
                                        data-caption-path="media/captions/MSI_06_03.vtt">Loading the Extension from a Remote Location</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_07_00.mp4"
                                data-media-path="media/video/MSI_07_00.mp4"
                                data-caption-path="media/captions/MSI_07_00.vtt">UDF Reverse Shell</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_08_00.mp4"
                                data-media-path="media/video/MSI_08_00.mp4"
                                data-caption-path="media/captions/MSI_08_00.vtt">More Shells!!!</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_08_01.mp4"
                                        data-media-path="media/video/MSI_08_01.mp4"
                                        data-caption-path="media/captions/MSI_08_01.vtt">PostgreSQL Large Objects</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/MSI_08_02.mp4"
                                        data-media-path="media/video/MSI_08_02.mp4"
                                        data-caption-path="media/captions/MSI_08_02.vtt">Large Object Reverse Shell</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/MSI_09_00.mp4"
                                data-media-path="media/video/MSI_09_00.mp4"
                                data-caption-path="media/captions/MSI_09_00.vtt">Summary</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/BCI_00_00.mp4"
                data-media-path="media/video/BCI_00_00.mp4" data-caption-path="media/captions/BCI_00_00.vtt">Bassmaster NodeJS Arbitrary JavaScript Injection Vulnerability</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/BCI_01_00.mp4"
                                data-media-path="media/video/BCI_01_00.mp4"
                                data-caption-path="media/captions/BCI_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/BCI_02_00.mp4"
                                data-media-path="media/video/BCI_02_00.mp4"
                                data-caption-path="media/captions/BCI_02_00.vtt">Vulnerability Discovery</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/BCI_03_00.mp4"
                                data-media-path="media/video/BCI_03_00.mp4"
                                data-caption-path="media/captions/BCI_03_00.vtt">Triggering the Vulnerability</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/BCI_04_00.mp4"
                                data-media-path="media/video/BCI_04_00.mp4"
                                data-caption-path="media/captions/BCI_04_00.vtt">Obtaining a Reverse Shell</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/BCI_05_00.mp4"
                                data-media-path="media/video/BCI_05_00.mp4"
                                data-caption-path="media/captions/BCI_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/DDR_00_00.mp4"
                data-media-path="media/video/DDR_00_00.mp4" data-caption-path="media/captions/DDR_00_00.vtt">DotNetNuke Cookie Deserialization RCE</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/DDR_01_00.mp4"
                                data-media-path="media/video/DDR_01_00.mp4"
                                data-caption-path="media/captions/DDR_01_00.vtt">Serialization Basics</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_01_01.mp4"
                                        data-media-path="media/video/DDR_01_01.mp4"
                                        data-caption-path="media/captions/DDR_01_01.vtt">XMLSerializer Limitations</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_01_02.mp4"
                                        data-media-path="media/video/DDR_01_02.mp4"
                                        data-caption-path="media/captions/DDR_01_02.vtt">Basic XMLSerializer Example</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_01_03.mp4"
                                        data-media-path="media/video/DDR_01_03.mp4"
                                        data-caption-path="media/captions/DDR_01_03.vtt">Expanded XMLSerializer Example</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_01_04.mp4"
                                        data-media-path="media/video/DDR_01_04.mp4"
                                        data-caption-path="media/captions/DDR_01_04.vtt">Watch your Type, Dude</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/DDR_02_00.mp4"
                                data-media-path="media/video/DDR_02_00.mp4"
                                data-caption-path="media/captions/DDR_02_00.vtt">DotNetNuke Vulnerability Analysis</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_02_01.mp4"
                                        data-media-path="media/video/DDR_02_01.mp4"
                                        data-caption-path="media/captions/DDR_02_01.vtt">Vulnerability Overview</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_02_02.mp4"
                                        data-media-path="media/video/DDR_02_02.mp4"
                                        data-caption-path="media/captions/DDR_02_02.vtt">Manipulation of Assembly Attributes for Debugging</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_02_03.mp4"
                                        data-media-path="media/video/DDR_02_03.mp4"
                                        data-caption-path="media/captions/DDR_02_03.vtt">Debugging DotNetNuke Using dnSpy</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_02_04.mp4"
                                        data-media-path="media/video/DDR_02_04.mp4"
                                        data-caption-path="media/captions/DDR_02_04.vtt">How Did We Get Here?</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/DDR_03_00.mp4"
                                data-media-path="media/video/DDR_03_00.mp4"
                                data-caption-path="media/captions/DDR_03_00.vtt">Payload Options</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_03_01.mp4"
                                        data-media-path="media/video/DDR_03_01.mp4"
                                        data-caption-path="media/captions/DDR_03_01.vtt">FileSystemUtils PullFile Method</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_03_02.mp4"
                                        data-media-path="media/video/DDR_03_02.mp4"
                                        data-caption-path="media/captions/DDR_03_02.vtt">ObjectDataProvider Class</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_03_03.mp4"
                                        data-media-path="media/video/DDR_03_03.mp4"
                                        data-caption-path="media/captions/DDR_03_03.vtt">Example Use of the ObjectDataProvider Instance</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_03_04.mp4"
                                        data-media-path="media/video/DDR_03_04.mp4"
                                        data-caption-path="media/captions/DDR_03_04.vtt">Serialization of the ObjectDataProvider</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/DDR_03_05.mp4"
                                        data-media-path="media/video/DDR_03_05.mp4"
                                        data-caption-path="media/captions/DDR_03_05.vtt">Enter The Dragon (ExpandedWrapper Class)</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/DDR_04_00.mp4"
                                data-media-path="media/video/DDR_04_00.mp4"
                                data-caption-path="media/captions/DDR_04_00.vtt">Putting It All Together</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/DDR_05_00.mp4"
                                data-media-path="media/video/DDR_05_00.mp4"
                                data-caption-path="media/captions/DDR_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/ERP_00_00.mp4"
                data-media-path="media/video/ERP_00_00.mp4" data-caption-path="media/captions/ERP_00_00.vtt">ERPNext Authentication Bypass and Server Side Template Injection</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_01_00.mp4"
                                data-media-path="media/video/ERP_01_00.mp4"
                                data-caption-path="media/captions/ERP_01_00.vtt">Getting Started</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_01_01.mp4"
                                        data-media-path="media/video/ERP_01_01.mp4"
                                        data-caption-path="media/captions/ERP_01_01.vtt">Configuring the SMTP Server</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_01_02.mp4"
                                        data-media-path="media/video/ERP_01_02.mp4"
                                        data-caption-path="media/captions/ERP_01_02.vtt">Configuring Remote Debugging</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_01_03.mp4"
                                        data-media-path="media/video/ERP_01_03.mp4"
                                        data-caption-path="media/captions/ERP_01_03.vtt">Configuring MariaDB Query Logging</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_02_00.mp4"
                                data-media-path="media/video/ERP_02_00.mp4"
                                data-caption-path="media/captions/ERP_02_00.vtt">Introduction to MVC, Metadata-Driven Architecture, and HTTP Routing</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_02_01.mp4"
                                        data-media-path="media/video/ERP_02_01.mp4"
                                        data-caption-path="media/captions/ERP_02_01.vtt">Model-View-Controller Introduction</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_02_02.mp4"
                                        data-media-path="media/video/ERP_02_02.mp4"
                                        data-caption-path="media/captions/ERP_02_02.vtt">Metadata-driven Design Patterns</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_02_03.mp4"
                                        data-media-path="media/video/ERP_02_03.mp4"
                                        data-caption-path="media/captions/ERP_02_03.vtt">HTTP Routing in Frappe</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_03_00.mp4"
                                data-media-path="media/video/ERP_03_00.mp4"
                                data-caption-path="media/captions/ERP_03_00.vtt">Authentication Bypass Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_03_01.mp4"
                                        data-media-path="media/video/ERP_03_01.mp4"
                                        data-caption-path="media/captions/ERP_03_01.vtt">Discovering the SQL Injection</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_04_00.mp4"
                                data-media-path="media/video/ERP_04_00.mp4"
                                data-caption-path="media/captions/ERP_04_00.vtt">Authentication Bypass Exploitation</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_04_01.mp4"
                                        data-media-path="media/video/ERP_04_01.mp4"
                                        data-caption-path="media/captions/ERP_04_01.vtt">Obtaining Admin User Information</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_04_02.mp4"
                                        data-media-path="media/video/ERP_04_02.mp4"
                                        data-caption-path="media/captions/ERP_04_02.vtt">Resetting the Admin Password</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_05_00.mp4"
                                data-media-path="media/video/ERP_05_00.mp4"
                                data-caption-path="media/captions/ERP_05_00.vtt">SSTI Vulnerability Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_05_01.mp4"
                                        data-media-path="media/video/ERP_05_01.mp4"
                                        data-caption-path="media/captions/ERP_05_01.vtt">Introduction to Templating Engines</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_05_02.mp4"
                                        data-media-path="media/video/ERP_05_02.mp4"
                                        data-caption-path="media/captions/ERP_05_02.vtt">Discovering The Rendering Function</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_05_03.mp4"
                                        data-media-path="media/video/ERP_05_03.mp4"
                                        data-caption-path="media/captions/ERP_05_03.vtt">SSTI Vulnerability Filter Evasion</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_06_00.mp4"
                                data-media-path="media/video/ERP_06_00.mp4"
                                data-caption-path="media/captions/ERP_06_00.vtt">SSTI Vulnerability Exploitation</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_06_01.mp4"
                                        data-media-path="media/video/ERP_06_01.mp4"
                                        data-caption-path="media/captions/ERP_06_01.vtt">Finding a Method for Remote Command Execution</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/ERP_06_02.mp4"
                                        data-media-path="media/video/ERP_06_02.mp4"
                                        data-caption-path="media/captions/ERP_06_02.vtt">Gaining Remote Command Execution</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/ERP_07_00.mp4"
                                data-media-path="media/video/ERP_07_00.mp4"
                                data-caption-path="media/captions/ERP_07_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/OCRX_00_00.mp4"
                data-media-path="media/video/OCRX_00_00.mp4" data-caption-path="media/captions/OCRX_00_00.vtt">openCRX
                Authentication Bypass
                and Remote Code Execution</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OCRX_01_00.mp4"
                                data-media-path="media/video/OCRX_01_00.mp4"
                                data-caption-path="media/captions/OCRX_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OCRX_02_00.mp4"
                                data-media-path="media/video/OCRX_02_00.mp4"
                                data-caption-path="media/captions/OCRX_02_00.vtt">Password Reset Vulnerability Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_02_01.mp4"
                                        data-media-path="media/video/OCRX_02_01.mp4"
                                        data-caption-path="media/captions/OCRX_02_01.vtt">When Random Isn't</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_02_02.mp4"
                                        data-media-path="media/video/OCRX_02_02.mp4"
                                        data-caption-path="media/captions/OCRX_02_02.vtt">Account Determination</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_02_03.mp4"
                                        data-media-path="media/video/OCRX_02_03.mp4"
                                        data-caption-path="media/captions/OCRX_02_03.vtt">Timing the Reset Request</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_02_04.mp4"
                                        data-media-path="media/video/OCRX_02_04.mp4"
                                        data-caption-path="media/captions/OCRX_02_04.vtt">Generate Token List</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_02_05.mp4"
                                        data-media-path="media/video/OCRX_02_05.mp4"
                                        data-caption-path="media/captions/OCRX_02_05.vtt">Automating Resets</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OCRX_03_00.mp4"
                                data-media-path="media/video/OCRX_03_00.mp4"
                                data-caption-path="media/captions/OCRX_03_00.vtt">XML External Entity Vulnerability Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_01.mp4"
                                        data-media-path="media/video/OCRX_03_01.mp4"
                                        data-caption-path="media/captions/OCRX_03_01.vtt">Introduction to XML</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_02.mp4"
                                        data-media-path="media/video/OCRX_03_02.mp4"
                                        data-caption-path="media/captions/OCRX_03_02.vtt">XML Parsing</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_03.mp4"
                                        data-media-path="media/video/OCRX_03_03.mp4"
                                        data-caption-path="media/captions/OCRX_03_03.vtt">XML Entities</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_04.mp4"
                                        data-media-path="media/video/OCRX_03_04.mp4"
                                        data-caption-path="media/captions/OCRX_03_04.vtt">Understanding XML External Entity Processing Vulnerabilities</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_05.mp4"
                                        data-media-path="media/video/OCRX_03_05.mp4"
                                        data-caption-path="media/captions/OCRX_03_05.vtt">Finding the Attack Vector</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_06.mp4"
                                        data-media-path="media/video/OCRX_03_06.mp4"
                                        data-caption-path="media/captions/OCRX_03_06.vtt">CDATA</a>
                        </li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_07.mp4"
                                        data-media-path="media/video/OCRX_03_07.mp4"
                                        data-caption-path="media/captions/OCRX_03_07.vtt">Updating the XXE Exploit</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_08.mp4"
                                        data-media-path="media/video/OCRX_03_08.mp4"
                                        data-caption-path="media/captions/OCRX_03_08.vtt">Gaining Remote Access to HSQLDB</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_03_09.mp4"
                                        data-media-path="media/video/OCRX_03_09.mp4"
                                        data-caption-path="media/captions/OCRX_03_09.vtt">Java Language Routines</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OCRX_04_00.mp4"
                                data-media-path="media/video/OCRX_04_00.mp4"
                                data-caption-path="media/captions/OCRX_04_00.vtt">Remote Code Execution</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_04_01.mp4"
                                        data-media-path="media/video/OCRX_04_01.mp4"
                                        data-caption-path="media/captions/OCRX_04_01.vtt">Finding the Write Location</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OCRX_04_02.mp4"
                                        data-media-path="media/video/OCRX_04_02.mp4"
                                        data-caption-path="media/captions/OCRX_04_02.vtt">Writing Web Shells</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OCRX_05_00.mp4"
                                data-media-path="media/video/OCRX_05_00.mp4"
                                data-caption-path="media/captions/OCRX_05_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/OPENIT_00_00.mp4"
                data-media-path="media/video/OPENIT_00_00.mp4"
                data-caption-path="media/captions/OPENIT_00_00.vtt">openITCOCKPIT XSS and OS Command Injection - Blackbox</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_01_00.mp4"
                                data-media-path="media/video/OPENIT_01_00.mp4"
                                data-caption-path="media/captions/OPENIT_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_02_00.mp4"
                                data-media-path="media/video/OPENIT_02_00.mp4"
                                data-caption-path="media/captions/OPENIT_02_00.vtt">Black Box Testing in openITCOCKPIT</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_03_00.mp4"
                                data-media-path="media/video/OPENIT_03_00.mp4"
                                data-caption-path="media/captions/OPENIT_03_00.vtt">Application Discovery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_03_01.mp4"
                                        data-media-path="media/video/OPENIT_03_01.mp4"
                                        data-caption-path="media/captions/OPENIT_03_01.vtt">Building a Sitemap</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_03_02.mp4"
                                        data-media-path="media/video/OPENIT_03_02.mp4"
                                        data-caption-path="media/captions/OPENIT_03_02.vtt">Targeted Discovery</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_04_00.mp4"
                                data-media-path="media/video/OPENIT_04_00.mp4"
                                data-caption-path="media/captions/OPENIT_04_00.vtt">Intro To DOM-based XSS</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_05_00.mp4"
                                data-media-path="media/video/OPENIT_05_00.mp4"
                                data-caption-path="media/captions/OPENIT_05_00.vtt">XSS Hunting</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_06_00.mp4"
                                data-media-path="media/video/OPENIT_06_00.mp4"
                                data-caption-path="media/captions/OPENIT_06_00.vtt">Advanced XSS Exploitation</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_01.mp4"
                                        data-media-path="media/video/OPENIT_06_01.mp4"
                                        data-caption-path="media/captions/OPENIT_06_01.vtt">What We Can and Can't Do</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_02.mp4"
                                        data-media-path="media/video/OPENIT_06_02.mp4"
                                        data-caption-path="media/captions/OPENIT_06_02.vtt">Writing to DOM</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_03.mp4"
                                        data-media-path="media/video/OPENIT_06_03.mp4"
                                        data-caption-path="media/captions/OPENIT_06_03.vtt">Creating the Database</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_04.mp4"
                                        data-media-path="media/video/OPENIT_06_04.mp4"
                                        data-caption-path="media/captions/OPENIT_06_04.vtt">Creating the API</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_05.mp4"
                                        data-media-path="media/video/OPENIT_06_05.mp4"
                                        data-caption-path="media/captions/OPENIT_06_05.vtt">Scraping Content</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_06_06.mp4"
                                        data-media-path="media/video/OPENIT_06_06.mp4"
                                        data-caption-path="media/captions/OPENIT_06_06.vtt">Dumping the Contents</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_07_00.mp4"
                                data-media-path="media/video/OPENIT_07_00.mp4"
                                data-caption-path="media/captions/OPENIT_07_00.vtt">RCE Hunting</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_07_01.mp4"
                                        data-media-path="media/video/OPENIT_07_01.mp4"
                                        data-caption-path="media/captions/OPENIT_07_01.vtt">Discovery</a>
                        </li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_07_02.mp4"
                                        data-media-path="media/video/OPENIT_07_02.mp4"
                                        data-caption-path="media/captions/OPENIT_07_02.vtt">Reading and Understanding the JavaScript</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_07_03.mp4"
                                        data-media-path="media/video/OPENIT_07_03.mp4"
                                        data-caption-path="media/captions/OPENIT_07_03.vtt">Interacting With the WebSocket Server</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_07_04.mp4"
                                        data-media-path="media/video/OPENIT_07_04.mp4"
                                        data-caption-path="media/captions/OPENIT_07_04.vtt">Building a Client</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/OPENIT_07_05.mp4"
                                        data-media-path="media/video/OPENIT_07_05.mp4"
                                        data-caption-path="media/captions/OPENIT_07_05.vtt">Digging Deeper</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/OPENIT_08_00.mp4"
                                data-media-path="media/video/OPENIT_08_00.mp4"
                                data-caption-path="media/captions/OPENIT_08_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/CORS_00_00.mp4"
                data-media-path="media/video/CORS_00_00.mp4" data-caption-path="media/captions/CORS_00_00.vtt">Concord Authentication Bypass to RCE</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/CORS_01_00.mp4"
                                data-media-path="media/video/CORS_01_00.mp4"
                                data-caption-path="media/captions/CORS_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/CORS_02_00.mp4"
                                data-media-path="media/video/CORS_02_00.mp4"
                                data-caption-path="media/captions/CORS_02_00.vtt">Authentication Bypass: Round One - CSRF and CORS</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/CORS_02_01.mp4"
                                        data-media-path="media/video/CORS_02_01.mp4"
                                        data-caption-path="media/captions/CORS_02_01.vtt">Same-Origin Policy (SOP)</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/CORS_02_02.mp4"
                                        data-media-path="media/video/CORS_02_02.mp4"
                                        data-caption-path="media/captions/CORS_02_02.vtt">Cross-Origin Resource Sharing (CORS)</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/CORS_02_03.mp4"
                                        data-media-path="media/video/CORS_02_03.mp4"
                                        data-caption-path="media/captions/CORS_02_03.vtt">Discovering Unsafe CORS Headers</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/CORS_02_04.mp4"
                                        data-media-path="media/video/CORS_02_04.mp4"
                                        data-caption-path="media/captions/CORS_02_04.vtt">SameSite Attribute</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/CORS_02_05.mp4"
                                        data-media-path="media/video/CORS_02_05.mp4"
                                        data-caption-path="media/captions/CORS_02_05.vtt">Exploit Permissive CORS and CSRF</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/CORS_03_00.mp4"
                                data-media-path="media/video/CORS_03_00.mp4"
                                data-caption-path="media/captions/CORS_03_00.vtt">Authentication Bypass: Round Two - Insecure Defaults</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/CORS_04_00.mp4"
                                data-media-path="media/video/CORS_04_00.mp4"
                                data-caption-path="media/captions/CORS_04_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/SSRF_00_00.mp4"
                data-media-path="media/video/SSRF_00_00.mp4" data-caption-path="media/captions/SSRF_00_00.vtt">Server Side Request Forgery</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_01_00.mp4"
                                data-media-path="media/video/SSRF_01_00.mp4"
                                data-caption-path="media/captions/SSRF_01_00.vtt">Getting Started</a>
                </li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_02_00.mp4"
                                data-media-path="media/video/SSRF_02_00.mp4"
                                data-caption-path="media/captions/SSRF_02_00.vtt">Introduction to Microservices</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_02_01.mp4"
                                        data-media-path="media/video/SSRF_02_01.mp4"
                                        data-caption-path="media/captions/SSRF_02_01.vtt">Web Service URL Formats</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_03_00.mp4"
                                data-media-path="media/video/SSRF_03_00.mp4"
                                data-caption-path="media/captions/SSRF_03_00.vtt">API Discovery via Verb Tampering</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_03_01.mp4"
                                        data-media-path="media/video/SSRF_03_01.mp4"
                                        data-caption-path="media/captions/SSRF_03_01.vtt">Initial Enumeration</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_03_02.mp4"
                                        data-media-path="media/video/SSRF_03_02.mp4"
                                        data-caption-path="media/captions/SSRF_03_02.vtt">Advanced Enumeration with Verb Tampering</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_04_00.mp4"
                                data-media-path="media/video/SSRF_04_00.mp4"
                                data-caption-path="media/captions/SSRF_04_00.vtt">Introduction to Server-Side Request Forgery</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_01.mp4"
                                        data-media-path="media/video/SSRF_04_01.mp4"
                                        data-caption-path="media/captions/SSRF_04_01.vtt">Server-Side Request Forgery Discovery</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_02.mp4"
                                        data-media-path="media/video/SSRF_04_02.mp4"
                                        data-caption-path="media/captions/SSRF_04_02.vtt">Source Code Analysis</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_03.mp4"
                                        data-media-path="media/video/SSRF_04_03.mp4"
                                        data-caption-path="media/captions/SSRF_04_03.vtt">Exploiting Blind SSRF in Directus</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_04.mp4"
                                        data-media-path="media/video/SSRF_04_04.mp4"
                                        data-caption-path="media/captions/SSRF_04_04.vtt">Port Scanning via Blind SSRF</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_05.mp4"
                                        data-media-path="media/video/SSRF_04_05.mp4"
                                        data-caption-path="media/captions/SSRF_04_05.vtt">Subnet Scanning with SSRF</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_04_06.mp4"
                                        data-media-path="media/video/SSRF_04_06.mp4"
                                        data-caption-path="media/captions/SSRF_04_06.vtt">Host Enumeration</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_05_00.mp4"
                                data-media-path="media/video/SSRF_05_00.mp4"
                                data-caption-path="media/captions/SSRF_05_00.vtt">Render API Auth Bypass</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_06_00.mp4"
                                data-media-path="media/video/SSRF_06_00.mp4"
                                data-caption-path="media/captions/SSRF_06_00.vtt">Exploiting Headless Chrome</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_06_01.mp4"
                                        data-media-path="media/video/SSRF_06_01.mp4"
                                        data-caption-path="media/captions/SSRF_06_01.vtt">Using JavaScript to Exfiltrate Data</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_06_02.mp4"
                                        data-media-path="media/video/SSRF_06_02.mp4"
                                        data-caption-path="media/captions/SSRF_06_02.vtt">Stealing Credentials from Kong Admin API</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_06_03.mp4"
                                        data-media-path="media/video/SSRF_06_03.mp4"
                                        data-caption-path="media/captions/SSRF_06_03.vtt">URL to PDF Microservice Source Code Analysis</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_07_00.mp4"
                                data-media-path="media/video/SSRF_07_00.mp4"
                                data-caption-path="media/captions/SSRF_07_00.vtt">Remote Code Execution</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/SSRF_07_01.mp4"
                                        data-media-path="media/video/SSRF_07_01.mp4"
                                        data-caption-path="media/captions/SSRF_07_01.vtt">RCE in Kong Admin API</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/SSRF_08_00.mp4"
                                data-media-path="media/video/SSRF_08_00.mp4"
                                data-caption-path="media/captions/SSRF_08_00.vtt">Wrapping Up</a></li>
        </ul>
</li>
<li class="module-title"><a class="module"
                href="https://xyz.website/media/video/PROTO_00_00.mp4"
                data-media-path="media/video/PROTO_00_00.mp4"
                data-caption-path="media/captions/PROTO_00_00.vtt">Guacamole Lite Prototype Pollution</a>
        <ul class="submenu">
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_01_00.mp4"
                                data-media-path="media/video/PROTO_01_00.mp4"
                                data-caption-path="media/captions/PROTO_01_00.vtt">Getting Started</a>
                </li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_01_01.mp4"
                                        data-media-path="media/video/PROTO_01_01.mp4"
                                        data-caption-path="media/captions/PROTO_01_01.vtt">Understanding the Code</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_01_02.mp4"
                                        data-media-path="media/video/PROTO_01_02.mp4"
                                        data-caption-path="media/captions/PROTO_01_02.vtt">Configuring Remote Debugging</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_02_00.mp4"
                                data-media-path="media/video/PROTO_02_00.mp4"
                                data-caption-path="media/captions/PROTO_02_00.vtt">Introduction to JavaScript Prototype</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_02_01.mp4"
                                        data-media-path="media/video/PROTO_02_01.mp4"
                                        data-caption-path="media/captions/PROTO_02_01.vtt">Prototype Pollution</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_02_02.mp4"
                                        data-media-path="media/video/PROTO_02_02.mp4"
                                        data-caption-path="media/captions/PROTO_02_02.vtt">Blackbox Discovery</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_02_03.mp4"
                                        data-media-path="media/video/PROTO_02_03.mp4"
                                        data-caption-path="media/captions/PROTO_02_03.vtt">Whitebox Discovery</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_03_00.mp4"
                                data-media-path="media/video/PROTO_03_00.mp4"
                                data-caption-path="media/captions/PROTO_03_00.vtt">Prototype Pollution Exploitation</a></li>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_04_00.mp4"
                                data-media-path="media/video/PROTO_04_00.mp4"
                                data-caption-path="media/captions/PROTO_04_00.vtt">EJS</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_04_01.mp4"
                                        data-media-path="media/video/PROTO_04_01.mp4"
                                        data-caption-path="media/captions/PROTO_04_01.vtt">EJS - Proof of Concept</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_04_02.mp4"
                                        data-media-path="media/video/PROTO_04_02.mp4"
                                        data-caption-path="media/captions/PROTO_04_02.vtt">EJS - Remote Code Execution</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_05_00.mp4"
                                data-media-path="media/video/PROTO_05_00.mp4"
                                data-caption-path="media/captions/PROTO_05_00.vtt">Handlebars</a></li>
                <ul class="subSection-menu">
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_05_01.mp4"
                                        data-media-path="media/video/PROTO_05_01.mp4"
                                        data-caption-path="media/captions/PROTO_05_01.vtt">Handlebars - Proof of Concept</a></li>
                        <li><a class="sub-module"
                                        href="https://xyz.website/media/video/PROTO_05_02.mp4"
                                        data-media-path="media/video/PROTO_05_02.mp4"
                                        data-caption-path="media/captions/PROTO_05_02.vtt">Handlebars - Remote Code Execution</a></li>
                </ul>
                <li><a class="sub-module"
                                href="https://xyz.website/media/video/PROTO_06_00.mp4"
                                data-media-path="media/video/PROTO_06_00.mp4"
                                data-caption-path="media/captions/PROTO_06_00.vtt">Wrapping Up</a></li>
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
            tempDict["Submodule"] = (
                submodule.find('a', class_='sub-module').text)
            sub_submodule_list = submodule.find('ul', class_='subSection-menu')
            if sub_submodule_list:
                sub_submodules = sub_submodule_list.find_all('li')
                for sub_submodule in sub_submodules:
                    tempDict["Sub-Submodule"] = (
                        sub_submodule.find('a', class_='sub-module').text)
                    tempDict["Href"] = (sub_submodule.find(
                        'a', class_='sub-module')['href'])
            else:
                tempDict["Href"] = submodule.find(
                    'a', class_='sub-module')['href']
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

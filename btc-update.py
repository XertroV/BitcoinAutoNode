#!/usr/bin/python
from bitcoinrpc.authproxy import AuthServiceProxy
import time

www_file = "/var/www/index.html"
rpc_user = ""
rpc_pass = ""
node_location = ""
node_name = ""
node_ip = ""
donation_btc_addr = ""

access = AuthServiceProxy("http://" + rpc_user + ":" + rpc_pass + "@127.0.0.1:8332")
info = access.getinfo()

ff = open(www_file, 'w')


ff.write("<!DOCTYPE html>")
ff.write("<html lang='en-us'>")
ff.write("<head>")
ff.write("<meta charset='utf-8'>")
ff.write("<title>Bitcoin Node Status</title>")
ff.write("<link href='http://fonts.googleapis.com/css?family=Exo+2:300,400' rel='stylesheet' type='text/css'>")
ff.write("<style type='text/css'> ")
ff.write("</style>")
ff.write("</head>")
ff.write("<body>")

ff.write("<link href='http://fonts.googleapis.com/css?family=Exo+2:300,400' rel='stylesheet' type='text/css'>")
ff.write("<style>")

ff.write("/* Eric Meyer's Reset CSS v2.0 - http://cssreset.com */")
ff.write("html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{border:0;font-size:100%;font:inherit;vertical-align:baseline;margin:0;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:none}table{border-collapse:collapse;border-spacing:0}")

ff.write("html,body{height:100%;}")
ff.write("body{")
ff.write("color: #444;")
ff.write("background: url(http://www.babayara.com/wp-content/uploads/2013/08/vlcsnap-2013-08-24-23h14m34s7.png) no-repeat;")
ff.write("}")

ff.write("#wrap{")
ff.write("background-color: rgba(255, 255, 255, 0.6);")
ff.write("width: 100%;")
ff.write("height: 100%;")
ff.write("padding-top: 50px;")
ff.write("padding-left: 50px;")
ff.write("line-height: 1.4;")
ff.write("font-size: 24px;")
ff.write("font-family: 'Exo 2', sans-serif;")
ff.write("}")

ff.write("h3{")
ff.write("font-weight: 300;")
ff.write("}")

ff.write("h1{")
ff.write("font-weight: 400;")
ff.write("margin-bottom: 15px;")
ff.write("}")
ff.write("</style>")
ff.write("<div id='wrap'>")
ff.write("<h1>Bitcoin Node: " + node_ip + ":8333<br \></h1>")
ff.write("<h3>")

ff.write("Last Update: " + time.strftime("%H:%M:%S %Y-%m-%d") + "<br \>\n")
ff.write("Connections: " + str(info['connections']) + "<br \>\n")
ff.write("Blocks: " + str(info['blocks']) + "<br \>\n")
ff.write("Difficulty: " + str(info['difficulty']) + "<br \>\n")

ff.write("Location: " + node_location + "<br />")
ff.write("Node created by " + node_name + "<br />")
ff.write("Donate: <a href='https://blockchain.info/address/" + donation_btc_addr + "'>")
ff.write(donation_btc_addr + "</a>")
ff.write("</h3>")

ff.write("<img src='http://qrfree.kaywa.com/?l=1&amp;s=4&amp;d=" + donation_btc_addr + "' alt='QRCode'>")
ff.write("</div>")
ff.write("</body></html>")

ff.close()

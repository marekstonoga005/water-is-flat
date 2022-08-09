import fetch from 'node-fetch'
import fs from 'fs'
let domainz={
    "forzahorizon5.ml":{
        email: "forzahorizon5ml@arxxwalls.com",
        pass: "yznt$sCrAd8G!wCp9$Eu"
    },
    "forzahorizon5.tk":{
        email: "forzahorizon5tk@arxxwalls.com",
        pass: "$$!Fvc5AgubCa!i#54#!"
    },
    "forzahorizon5.ga":{
        email: "forzahorizon5ga@arxxwalls.com",
        pass: "Fr9nIa$lnl#c#2G5wGif"
    },
    "forzahorizon5.gq":{
        email: "forzahorizon5gq@arxxwalls.com",
        pass: "~q9iC9nrg5!ny1$#e$wc"
    },
    "forzahorizon5.cf":{
        email: "forzahorizon5cf@arxxwalls.com",
        pass: "l1ylrgoDc8~geFFs#%qI"
    },
    "unturnedrp.tk":{
        email: "unturnedrptk@arxxwalls.com",
        pass: "auFB!Hy9AzA#~$#BwA77"
    },
    "unturnedrp.ml":{
        email: "unturnedrpml@arxxwalls.com",
        pass: "$&FIjd1q~&mGhgfzpvgh"
    },
    "highrp.tk":{
        email: "highrptk@arxxwalls.com",
        pass: "&5obHkBjoCyHt76zFb3&"
    },
    "highrp.ml":{
        email: "highrpml@arxxwalls.com",
        pass: "B0uwg$C$gf#ub~B5Buen"
    },
    "highrp.ga":{
        email: "highrpga@arxxwalls.com",
        pass: "r~6wso1032$l~7Hn0j%n"
    },
    "highrp.cf":{
        email: "highrpcf@arxxwalls.com",
        pass: "ov&13ee#2!&Ed$Eo#w&7"
    },
    "highrp.gq":{
        email: "highrpgq@arxxwalls.com",
        pass: "$rnj4e%wn2q7d%~i%ict"
    },
    "stolicarp.tk":{
        email: "stolicarptk@arxxwalls.com",
        pass: "G5ldboGeFgny2IcAH~13"
    },
    "stolicarp.ml":{
        email: "stolicarpml@arxxwalls.com",
        pass: "HDn!6Gvokfvrbg#GhIgm"
    },
    "stolicarp.ga":{
        email: "stolicarpga@arxxwalls.com",
        pass: "$4d5&r0pEl4hk911vzF0"
    },
    "stolicarp.cf":{
        email: "stolicarpcf@arxxwalls.com",
        pass: "394rgd%~e3xd#3lx#%l3"
    },
    "stolicarp.gq":{
        email: "stolicarpgq@arxxwalls.com",
        pass: "0!2H#C$%bizG8rw15qgd"
    },
    "txtl.ml":{
        email: "txtlml@arxxwalls.com",
        pass: "%iDz6a~trhmvq#%!919$"
    },
    "txtl.tk":{
        email: "txtltk@arxxwalls.com",
        pass: "dAw&Gx#k7#jvGDq2#k0t"
    },
    "txtl.ga":{
        email: "txtlga@arxxwalls.com",
        pass: "Io&u!w1#~mE#25CaEmAo"
    },
    "txtl.cf":{
        email: "txtlcf@arxxwalls.com",
        pass: "G$b23Hy7I~&227~%cdG1"
    },
    "txtl.gq":{
        email: "txtlgq@arxxwalls.com",
        pass: "&&3Fs#5f!m2!p9piz7gF"
    },
    
}



const data = fs.readFileSync('a.txt', 'utf8');
let usee = domainz[data.split("\n")[0].split("@")[1]]
let mail = data.split("\n")[0]
console.log(mail)

fetch("https://api.mail.tm/token", {
    "headers": {
        "Content-Type": "application/json",
    },
    "body": "{\n  \"address\": \""+usee.email+"\",\n  \"password\": \""+usee.pass+"\"\n}",
    "method": "POST"
}).then(e=>{e.json().then(e=>{
    let token = e.token
    fetch("https://api.mail.tm/messages?page=1", {
        "headers": {
            "Authorization": "Bearer "+token
        },
        "method": "GET"
    }).then(e=>{e.json().then(e=>{
        e["hydra:member"].forEach(e => {
            console.log(e.to)
            if(e.to == ""){
            }else{

                if(e.to[0].address==mail){
                    
                    let impid = e.id
                    fetch("https://api.mail.tm/messages/"+impid, {
                                "credentials": "include",
                                "headers": {
                                    "Authorization": "Bearer "+token
                                },
                                "method": "DELETE",
                            });
                    fetch("https://api.mail.tm/messages/"+impid, {
                        "credentials": "include",
                        "headers": {
                            "Authorization": "Bearer "+token
                        },
                        "method": "GET"
                    }).then(e=>{e.json().then(e=>{
                        e.text.split("\n").forEach(e=>{
                            if(e.startsWith("Verify your email")){
                                e = e.replace("Verify your email ( ", "")
                                e = e.replace(" )", "")
                                fs.writeFile('a.txt', e, function (err,data) {});
                            }
                            
                        })
                    })})
                }
            }
        });
    })})
})})

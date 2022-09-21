import fetch from 'node-fetch'
import fs from 'fs'
let gmel={
    "stodolamarek1x":{
        email: "cloudy1@arxxwalls.com",
        pass: "cloudy123"
    },
    "stodolatomek1x":{
        email: "cloudy2@arxxwalls.com",
        pass: "cloudy123"
    },
    "stodolamaciek1x":{
        email: "cloudy3@arxxwalls.com",
        pass: "cloudy123"
    },
    "paruwczakp":{
        email: "cloudy4@arxxwalls.com",
        pass: "cloudy123"
    },
    "paruwczakq1":{
        email: "cloudy5@arxxwalls.com",
        pass: "cloudy123"
    },
    "paruwczakq2":{
        email: "cloudy6@arxxwalls.com",
        pass: "cloudy123"
    },
    "paruwczakq3":{
        email: "cloudy7@arxxwalls.com",
        pass: "cloudy123"
    }
}
let domains = {"forzahorizon5.ml":{"username":"forzahorizon5ml@arxxwalls.com","password":"yznt$sCrAd8G!wCp9$Eu"},"forzahorizon5.tk":{"username":"forzahorizon5tk@arxxwalls.com","password":"$$!Fvc5AgubCa!i#54#!"},"forzahorizon5.ga":{"username":"forzahorizon5ga@arxxwalls.com","password":"Fr9nIa$lnl#c#2G5wGif"},"forzahorizon5.gq":{"username":"forzahorizon5gq@arxxwalls.com","password":"~q9iC9nrg5!ny1$#e$wc"},"forzahorizon5.cf":{"username":"forzahorizon5cf@arxxwalls.com","password":"l1ylrgoDc8~geFFs#%qI"},"unturnedrp.tk":{"username":"unturnedrptk@arxxwalls.com","password":"auFB!Hy9AzA#~$#BwA77"},"unturnedrp.ml":{"username":"unturnedrpml@arxxwalls.com","password":"$&FIjd1q~&mGhgfzpvgh"},"highrp.tk":{"username":"highrptk@arxxwalls.com","password":"&5obHkBjoCyHt76zFb3&"},"highrp.ml":{"username":"highrpml@arxxwalls.com","password":"B0uwg$C$gf#ub~B5Buen"},"highrp.ga":{"username":"highrpga@arxxwalls.com","password":"r~6wso1032$l~7Hn0j%n"},"highrp.cf":{"username":"highrpcf@arxxwalls.com","password":"ov&13ee#2!&Ed$Eo#w&7"},"highrp.gq":{"username":"highrpgq@arxxwalls.com","password":"$rnj4e%wn2q7d%~i%ict"},"stolicarp.tk":{"username":"stolicarptk@arxxwalls.com","password":"G5ldboGeFgny2IcAH~13"},"stolicarp.ml":{"username":"stolicarpml@arxxwalls.com","password":"HDn!6Gvokfvrbg#GhIgm"},"stolicarp.ga":{"username":"stolicarpga@arxxwalls.com","password":"$4d5&r0pEl4hk911vzF0"},"stolicarp.cf":{"username":"stolicarpcf@arxxwalls.com","password":"394rgd%~e3xd#3lx#%l3"},"stolicarp.gq":{"username":"stolicarpgq@arxxwalls.com","password":"0!2H#C$%bizG8rw15qgd"},"txtl.ml":{"username":"txtlml@arxxwalls.com","password":"%iDz6a~trhmvq#%!919$"},"txtl.tk":{"username":"txtltk@arxxwalls.com","password":"dAw&Gx#k7#jvGDq2#k0t"},"txtl.ga":{"username":"txtlga@arxxwalls.com","password":"Io&u!w1#~mE#25CaEmAo"},"txtl.cf":{"username":"txtlcf@arxxwalls.com","password":"G$b23Hy7I~&227~%cdG1"},"txtl.gq":{"username":"txtlgq@arxxwalls.com","password":"&&3Fs#5f!m2!p9piz7gF"}}


let data = fs.readFileSync('a.txt', 'utf8');
data =  data.split("\n")[0].split("|")
let mail = data[1]
let use = gmel[mail.split("+")[0]]
console.log(mail)

if(data[0]=="gmel"){
fetch("https://api.mail.tm/token", {
    "headers": {
        "Content-Type": "application/json",
    },
    "body": "{\n  \"address\": \""+use.email+"\",\n  \"password\": \""+use.pass+"\"\n}",
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
                        "method": "GET"
                    }).then(e=>{e.json().then(e=>{
                        fetch("https://api.mail.tm/messages/"+impid, {
                            "credentials": "include",
                            "headers": {
                                "Authorization": "Bearer "+token
                            },
                            "method": "DELETE",
                        });
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
}

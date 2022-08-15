import fetch from 'node-fetch'
import fs from 'fs'
let domainz={
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



const data = fs.readFileSync('a.txt', 'utf8');
let usee = domainz[data.split("\n")[0].split("+")[0]]
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

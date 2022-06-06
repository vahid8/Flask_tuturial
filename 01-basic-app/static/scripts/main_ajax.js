'use strict'

document.addEventListener('DOMContentLoaded', function(e) {

    const getBtn = document.querySelector('#getBtn');
    const postBtn = document.querySelector('#postBtn');
    const ageText = document.querySelector('#ageText');

    getBtn.addEventListener('click', function(){
        // Create an AJAX Call (GET)
        const getRequest = new XMLHttpRequest(); //create a new object
        getRequest.open('Get', '/myAge');
        getRequest.send();
        getRequest.addEventListener('load', function(e){
            const data = JSON.parse(this.response);
            ageText.innerHTML = data.Age;
        });
    });


    postBtn.addEventListener('click', function(){
        // Create an AJAX Call (POST)
        const postRequest = new XMLHttpRequest(); //create a new object
        postRequest.open('POST', '/myAge');
        let sendData = JSON.stringify({"newAge": 30});
        postRequest.send(sendData);
        postRequest.addEventListener('load', function(e){
            const getData = JSON.parse(this.response);
            console.log(getData.log);
        })
    });






});
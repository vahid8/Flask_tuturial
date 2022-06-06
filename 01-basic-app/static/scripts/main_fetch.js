'use strict'

document.addEventListener('DOMContentLoaded', function(e) {

    const getBtn = document.querySelector('#getBtn');
    const postBtn = document.querySelector('#postBtn');
    const ageText = document.querySelector('#ageText');

    getBtn.addEventListener('click', function(){
        fetch('/myAge').then(function(response){
            if (response.ok) {
                return response.json();
            }
            else {
                return Promise.reject(response);
            }
        }).then(function(data){
            ageText.innerHTML = data.Age;
        }).catch(function (error) {
	        console.warn('Something went wrong.', error);
        });
    });


    postBtn.addEventListener('click', function(){
        let sendData = JSON.stringify({"newAge": 30});

        fetch('/myAge', {method: 'POST', body: sendData, headers: {'Content-type': 'application/json; charset=UTF-8'}})
        .then(function(response){
            return response.json();
        }).then(function(data){
            console.log(data.log);
        })
    });


});
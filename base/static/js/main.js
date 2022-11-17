document.getElementById('bars').addEventListener('click', function(){
    document.getElementById('open').classList.toggle('hide');
    document.getElementById('nav_dropdown').classList.toggle('hide');
})






// to confirm tha an oder placed only for address page


//  this code is for order page styles for small pages and for staff profile page 
var order_all = document.getElementById('orders_all').addEventListener('click', function(){
    document.getElementById('open_display').style.display = 'none';

    document.getElementById('all_display').style.display = 'flex';
    document.getElementById('span_all').classList.add('span_style');
    document.getElementById('span_all').classList.toggle('initial_style');
    document.getElementById('span_open').classList.remove('span_style1');
})
var order_open = document.getElementById('orders_open').addEventListener('click', function(){
    document.getElementById('open_display').style.display = 'flex';
    document.getElementById('open_display').style.zIndex = '10';
    document.getElementById('all_display').style.display = 'none';
    document.getElementById('span_all').classList.remove('span_style');
    document.getElementById('span_all').classList.remove('initial_style');
    document.getElementById('span_open').classList.add('span_style1');

})

//  this is only for password input field verification





function validate(){
    var pass = document.getElementById("id_password1")
    var upper = document.getElementById("upper")
    var lower = document.getElementById("lower")
    var length = document.getElementById("length")
    var number = document.getElementById("number")

    if(pass.value.match(/[0-9]/)){
        number.style.color = "green"
    }
    else{
        number.style.color = "red"
    }

    if(pass.value.match(/[A-Z]/)){
        upper.style.color = "green"
    }
    else{
        upper.style.color = "red"
    }

    if(pass.value.match(/[a-z]/)){
        lower.style.color = "green"
    }
    else{
        lower.style.color = "red"
    }
    if(pass.value.length>=8){
        length.style.color = "green"
    }
    else{
        length.style.color = "red"
    }

}






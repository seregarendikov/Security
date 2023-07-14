// var number; //создаем переменную
// number = 10; //присваиваем значение
// document.querySelector("h1").innerHTML = number;
// var stroka = 'Привет'
// console.log(number + 10 + ' yello', stroka);
// document.write(number + 10 + ' yello', stroka);



function countRabbits() {
   
   var x = document.querySelector("textarea.text_sz").value;
   var a;
   a = x.split(' ');
   for(var i = 0; i<a.length; i++) {

      if(a[i] == 'geoloc') {
         a[i] = document.querySelector(".name_g").value;
     
      }     
      if(a[i] == 'security') {
         a[i] = document.querySelector(".name_s").value;
     
      }     
      if(a[i] == 'company') {
         a[i] = document.querySelector(".name_com").value;
        
      }     
      if(a[i] == 'name') {
         a[i] = document.querySelector(".name_n").value;
        
      }
      if(a[i] == 'propusk') {
         a[i] = document.querySelector(".name_p").value;
      }
      if(a[i] == 'date,') {
         a[i] = document.querySelector(".name_d").value;
            
      }   
      document.querySelector("textarea").innerHTML = a.join(' ');

   }  
   
      
   
}
var check = document.querySelector('.box-avto');
var avto_input = document.querySelector('.block-avto');

function Chek() {
   const style = avto_input.style
   const ischek = check.checked
   if (ischek){
      
      style.display = 'block';
   }else{
      style.display = 'none';
   }
  
}
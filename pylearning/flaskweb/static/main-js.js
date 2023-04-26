// image 마우스 이벤트
let pic = document.getElementById('pic');

pic.addEventListener('mouseover', function(){
    pic.src = '../static/coffee-gray.jpg';
});

pic.addEventListener('mouseout', function(){
    pic.src = '../static/coffee-blue.jpg';
});

/*
pic.onmouseover = changePic;
pic.onmouseout = originPic;

function changePic(){
    pic.src = '../static/coffee-gray.jpg';
}

function originPic(){
    pic.src = '../static/coffee-blue.jpg';
}
*/
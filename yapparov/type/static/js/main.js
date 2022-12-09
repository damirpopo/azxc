let select = document.getElementById('select');
let block = document.querySelectorAll('.block');
let lastIndex = 0;
select.addEventListener('change', function() {
  block[lastIndex].style.display = "none"; 
  let index = select.selectedIndex; 
  block[index].style.display = "block";

  lastIndex = index;
});
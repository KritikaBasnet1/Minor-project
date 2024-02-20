const boxes = document.querySelectorAll('.box')

// boxex.forEach((box) => {
//   box.addEventListener('click', (e) => {
//     // if (e.target.parentElement.classList.contains('spot-booked')) {
//     //   document.querySelector('.booked-model-wrapper').style.display = 'block'
//     // }
//     // if (e.target.parentElement.classList.contains('spot-occupied')) {
//     //   document.querySelector('.occupied-model-wrapper').style.display = 'block'
//     // }
//   })
// })

boxes.forEach((box)=>{
  box.addEventListener("click", ()=>{
document.querySelector('.login-model-wrapper').style.display = "block"
  })
})

document.querySelectorAll('.fa-x').forEach((x) => {
  x.addEventListener('click', () => {
    x.parentElement.parentElement.style.display = 'none'
  })
});


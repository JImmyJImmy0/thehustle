const dateInput = document.getElementById('id_date')

const picker = MCDatepicker.create({
    el: '#id_date',
    dateFormat: 'yyyy-mm-dd',
    closeOnBlur: true,
    autoClose: true,
    selectedDate: new Date(),
})

dateInput.addEventListener('click', (evt) => {
    picker.open()
})

console.log('working')
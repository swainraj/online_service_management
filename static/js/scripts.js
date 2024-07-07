document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            let valid = true;
            const inputs = form.querySelectorAll('input');
            
            inputs.forEach(input => {
                if (input.value.trim() === '') {
                    valid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });

            if (!valid) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    });
});

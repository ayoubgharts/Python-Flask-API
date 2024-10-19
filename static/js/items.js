// JavaScript for handling copy button functionality in items table
document.addEventListener('DOMContentLoaded', () => {
    // Select all copy buttons
    const copyButtons = document.querySelectorAll('.copy');
    const copiedButtons = document.querySelectorAll('.copied');

    // Hide all copied buttons initially
    copiedButtons.forEach(button => button.style.display = 'none');

    // Add click event listener for each copy button
    copyButtons.forEach((button, index) => {
        button.addEventListener('click', async () => {
            const idText = button.closest('tr').querySelector('td a.link').innerText;

            try {
                // Copy the ID text to clipboard
                await navigator.clipboard.writeText(idText);

                // Show the copied button and hide the copy button
                button.style.display = 'none';
                copiedButtons[index].style.display = 'inline-block';

                // Revert back to the original button after 3 seconds
                setTimeout(() => {
                    button.style.display = 'inline-block';
                    copiedButtons[index].style.display = 'none';
                }, 3000);

            } catch (err) {
                console.error('Failed to copy:', err);
            }
        });
    });
});

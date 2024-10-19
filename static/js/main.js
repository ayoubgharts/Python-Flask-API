async function copyToClipboard(button) {
    const apiLink = button.parentElement.previousElementSibling; // Get the previous sibling (the link)
    const textToCopy = apiLink.innerText; // Get the text to copy

    try {
        await navigator.clipboard.writeText(textToCopy); // Use the Clipboard API to write text

        // Change button to 'Copied' state
        button.innerHTML = `<i class="fa-solid fa-check"></i> Copied`;
        button.classList.add('copied');
        button.disabled = true; // Disable button to prevent multiple clicks

        // Revert back to original button after 3 seconds
        setTimeout(() => {
            button.innerHTML = `<i class="fa-regular fa-copy"></i>`;
            button.classList.remove('copied');
            button.disabled = false; // Enable button again
        }, 3000);

    } catch (err) {
        console.error('Failed to copy: ', err); // Log any errors
    } 
}

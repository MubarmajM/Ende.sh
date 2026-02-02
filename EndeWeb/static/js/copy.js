async function copy(tag_id) {
    var copyText = document.getElementById(tag_id);
    if (!copyText) {
        console.error('Element not found');
        alert('Element not found. Cannot copy.');
        return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
        try {
            await navigator.clipboard.writeText(copyText.innerText);
            console.log('Copied to clipboard'); 
        } catch (err) {
            console.error('Failed to copy: ', err);
            fallbackCopy(copyText);
        }
    } else {
        fallbackCopy(copyText);
    }
}

function fallbackCopy(element) {
    var textArea = document.createElement("textarea");
    textArea.value = element.innerText;
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
        document.execCommand('copy');
        console.log('Copied using fallback');
        //alert('Copied to clipboard using fallback method.');
    } catch (err) {
        console.error('Fallback copy failed: ', err);
        alert('Failed to copy text. Please copy manually.');
    }
    document.body.removeChild(textArea);
}
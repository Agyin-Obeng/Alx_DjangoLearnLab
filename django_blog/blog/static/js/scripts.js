document.addEventListener('DOMContentLoaded', () => {
    console.log('Blog page loaded');

    // ------------------------------------
    // 1. Highlight active nav link
    // ------------------------------------
    const links = document.querySelectorAll('header nav ul li a');
    links.forEach(link => {
        if (link.href === window.location.href) {
            link.style.fontWeight = 'bold';
            link.style.textDecoration = 'underline';
        }
    });

    // ------------------------------------
    // 2. Add a simple Back-to-Top button
    // (Styled with JS so CSS file stays untouched)
    // ------------------------------------
    const btn = document.createElement('button');
    btn.textContent = "↑ Top";
    btn.style.position = "fixed";
    btn.style.bottom = "20px";
    btn.style.right = "20px";
    btn.style.padding = "10px 15px";
    btn.style.backgroundColor = "#333";
    btn.style.color = "white";
    btn.style.border = "none";
    btn.style.borderRadius = "5px";
    btn.style.cursor = "pointer";
    btn.style.display = "none";
    btn.style.fontSize = "14px";
    btn.style.zIndex = "1000";

    document.body.appendChild(btn);

    // Show button when user scrolls
    window.addEventListener('scroll', () => {
        if (window.scrollY > 200) {
            btn.style.display = "block";
        } else {
            btn.style.display = "none";
        }
    });

    // Scroll to top when clicked
    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});

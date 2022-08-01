const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

sr.reveal('.about .about-content .img',{delay:500,origin:'left'})
sr.reveal('.prod .card',{delay:400})
sr.reveal('.about p.para',{delay:500,origin:'right'})
sr.reveal('.parallax h2.title',{})
sr.reveal('.gallery .item img',{delay:400})
sr.reveal('.new .new-content .img',{delay:400,origin:'left'})
sr.reveal('.contactForm',{delay:500,origin:'right'})
sr.reveal('.new p.para',{delay:400,origin:'right'})
sr.reveal('.contai .contactInfo .box .icon',{delay:100})
sr.reveal('.contai .contactInfo .box .text h3',{delay:100})
sr.reveal('.contai .contactInfo .box .text',{delay:100})
sr.reveal('footer .social-links ul li a span',{delay:100})
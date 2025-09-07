// Sistema de Tema
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Carregar tema salvo ou usar tema padrão
const savedTheme = localStorage.getItem('theme') || 'dark';
body.setAttribute('data-theme', savedTheme);
updateThemeIcon(savedTheme);

// Alternar tema
themeToggle.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
    
    // Animação de transição
    body.style.transition = 'all 0.3s ease';
    setTimeout(() => {
        body.style.transition = '';
    }, 300);
});

function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector('i');
    icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
}

// Menu Hamburger Dropdown Toggle
const hamburger = document.getElementById('hamburger-menu');
const navDropdown = document.getElementById('nav-dropdown');

function toggleMenu() {
    hamburger.classList.toggle('active');
    navDropdown.classList.toggle('active');
}

function closeMenu() {
    hamburger.classList.remove('active');
    navDropdown.classList.remove('active');
}

hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMenu();
});

// Fechar menu ao clicar fora dele
document.addEventListener('click', (e) => {
    if (!navDropdown.contains(e.target) && !hamburger.contains(e.target)) {
        closeMenu();
    }
});

// Fechar menu ao clicar em um link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', closeMenu));

// Fechar menu ao pressionar ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navDropdown.classList.contains('active')) {
        closeMenu();
    }
});

// Smooth scroll para âncoras
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Highlight do menu ativo baseado na seção visível
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('.content-section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Sistema de Partículas
function createParticles() {
    const particlesContainer = document.getElementById('particles');
    if (!particlesContainer) return;
    
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Posição aleatória
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        
        // Tamanho aleatório
        const size = Math.random() * 4 + 2;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        
        // Animação aleatória
        const duration = Math.random() * 6 + 3;
        const delay = Math.random() * 3;
        particle.style.animationDuration = duration + 's';
        particle.style.animationDelay = delay + 's';
        
        particlesContainer.appendChild(particle);
    }
}

// Contador Animado
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    function updateCounter() {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start).toLocaleString();
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target.toLocaleString();
        }
    }
    
    updateCounter();
}

// Inicializar contadores quando visíveis
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px 0px -50px 0px'
};

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = parseInt(entry.target.dataset.target);
            animateCounter(entry.target, target);
            counterObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observar elementos para animação
const animationObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

// Demo Interativo
function initInteractiveDemo() {
    const demoWindow = document.querySelector('.demo-window');
    const demoTrojan = document.querySelector('.demo-trojan');
    
    if (!demoWindow || !demoTrojan) return;
    
    demoWindow.addEventListener('click', () => {
        demoTrojan.classList.add('show');
        
        // Efeito de "infecção"
        demoWindow.style.filter = 'hue-rotate(120deg) saturate(2)';
        demoWindow.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
            demoTrojan.classList.remove('show');
            demoWindow.style.filter = '';
            demoWindow.style.transform = '';
        }, 3000);
    });
}

// Efeito de Digitação
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Efeito Parallax
function initParallax() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        const particles = document.querySelectorAll('.particle');
        
        // Aplicar parallax apenas se a seção hero estiver visível
        if (hero && scrolled < window.innerHeight) {
            hero.style.transform = `translateY(${scrolled * 0.1}px)`;
        } else if (hero) {
            hero.style.transform = 'translateY(0)';
        }
        
        particles.forEach((particle, index) => {
            const speed = 0.2 + (index % 3) * 0.1;
            particle.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
}

// Efeitos de Hover Avançados
function initHoverEffects() {
    // Cards com efeito de elevação
    document.querySelectorAll('.example-card, .action-card, .curiosity-item, .method-item, .language-item, .prop-item').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.03)';
            this.style.boxShadow = '0 20px 40px var(--shadow-medium)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 5px 20px var(--shadow-light)';
        });
    });
    
    // Imagens com zoom
    document.querySelectorAll('.hover-zoom').forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
            this.style.filter = 'brightness(1.2) contrast(1.1)';
        });
        
        img.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.filter = 'brightness(1) contrast(1)';
        });
    });
}

// Scroll Indicator
function initScrollIndicator() {
    const scrollIndicator = document.querySelector('.scroll-indicator');
    
    if (scrollIndicator) {
        scrollIndicator.addEventListener('click', () => {
            document.querySelector('.main-content').scrollIntoView({
                behavior: 'smooth'
            });
        });
    }
}

// Tooltip System
function initTooltips() {
    document.querySelectorAll('[data-tooltip]').forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.dataset.tooltip;
            tooltip.style.cssText = `
                position: absolute;
                background: var(--accent-secondary);
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                font-size: 14px;
                z-index: 1000;
                pointer-events: none;
                opacity: 0;
                transition: opacity 0.3s ease;
            `;
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 5 + 'px';
            
            setTimeout(() => tooltip.classList.add('show'), 10);
        });
        
        element.addEventListener('mouseleave', function() {
            const tooltip = document.querySelector('.tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });
}

// Loading Animation
function showLoading() {
    const loading = document.createElement('div');
    loading.className = 'loading';
    loading.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
    `;
    document.body.appendChild(loading);
    
    setTimeout(() => {
        loading.remove();
    }, 2000);
}

// Efeito de Cursor Personalizado - REMOVIDO

// Sistema de Notificações
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--accent-primary);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        box-shadow: 0 10px 30px var(--shadow-medium);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Efeito de Digitação no Título
function initTypingEffect() {
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        heroTitle.textContent = '';
        
        let i = 0;
        function type() {
            if (i < originalText.length) {
                heroTitle.textContent += originalText.charAt(i);
                
                // Adicionar classe 'loaded' para ativar o brilho progressivamente
                heroTitle.classList.add('loaded');
                
                i++;
                setTimeout(type, 100);
            }
        }
        
        // Iniciar a digitação após um pequeno delay
        setTimeout(type, 500);
    }
}

// Inicialização quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    // Inicializar todos os sistemas
    createParticles();
    initInteractiveDemo();
    initParallax();
    initHoverEffects();
    initScrollIndicator();
    initTooltips();
    initTypingEffect();
    
    // Observar elementos para animação
    document.querySelectorAll('.content-card, .example-card, .method-item, .action-card, .curiosity-item, .language-item, .prop-item').forEach(el => {
        el.classList.add('animate-on-scroll');
        animationObserver.observe(el);
    });
    
    // Observar contadores
    document.querySelectorAll('.stat-number').forEach(counter => {
        counterObserver.observe(counter);
    });
    
    
    // Efeito de entrada suave
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Efeito de clique nos cards
document.addEventListener('click', (e) => {
    if (e.target.closest('.example-card, .action-card, .curiosity-item')) {
        const card = e.target.closest('.example-card, .action-card, .curiosity-item');
        card.style.transform = 'scale(0.95)';
        setTimeout(() => {
            card.style.transform = '';
        }, 150);
    }
});

// Efeito de scroll suave para o indicador
window.addEventListener('scroll', () => {
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        if (window.scrollY > 100) {
            scrollIndicator.style.opacity = '0';
        } else {
            scrollIndicator.style.opacity = '1';
        }
    }
});

// Efeito de brilho nos ícones
document.querySelectorAll('.section-title i, .method-item i, .action-card i').forEach(icon => {
    icon.addEventListener('mouseenter', function() {
        this.style.textShadow = '0 0 20px var(--accent-primary)';
        this.style.transform = 'scale(1.2) rotate(10deg)';
    });
    
    icon.addEventListener('mouseleave', function() {
        this.style.textShadow = 'none';
        this.style.transform = 'scale(1) rotate(0deg)';
    });
});

// Sistema de Easter Eggs
let clickCount = 0;
document.querySelector('.hero-image').addEventListener('click', () => {
    clickCount++;
    if (clickCount === 5) {
        showNotification('Easter Egg descoberto! 🎉 Você é um verdadeiro especialista em segurança!', 'success');
        clickCount = 0;
    }
});

// Efeito de partículas no cursor - REMOVIDO
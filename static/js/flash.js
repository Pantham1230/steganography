// Auto-dismiss flash messages + click to dismiss
document.addEventListener('DOMContentLoaded', function() {
  const flashMessages = document.querySelectorAll('.flash-message');
  
  flashMessages.forEach((msg, index) => {
    // Auto-dismiss after 4 seconds
    setTimeout(() => {
      msg.style.animation = 'slideOutRight 0.4s ease forwards';
      setTimeout(() => msg.remove(), 400);
    }, 4000 + (index * 200)); // Staggered dismiss
    
    // Click to dismiss
    msg.addEventListener('click', () => {
      msg.style.animation = 'slideOutRight 0.3s ease forwards';
      setTimeout(() => msg.remove(), 300);
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
    const pentagramDiv = document.getElementById('pentagram');
    const subtopicsDiv = document.getElementById('subtopics');
    const contentDiv = document.getElementById('content');

    // Set up Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, pentagramDiv.clientWidth / pentagramDiv.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(pentagramDiv.clientWidth, pentagramDiv.clientHeight);
    pentagramDiv.appendChild(renderer.domElement);
// Create pentagram
const geometry = new THREE.BufferGeometry();
const vertices = [];
const radius = 0.8;
const innerRadius = 0.3;
for (let i = 0; i < 5; i++) {
    const angle = (i * 4 * Math.PI) / 5;
    const nextAngle = ((i + 1) * 4 * Math.PI) / 5;
    
    // Outer point
    vertices.push(radius * Math.cos(angle), radius * Math.sin(angle), 0);
    
    // Inner point
    vertices.push(innerRadius * Math.cos(nextAngle - Math.PI/5), innerRadius * Math.sin(nextAngle - Math.PI/5), 0);
}
// Close the shape
vertices.push(vertices[0], vertices[1], vertices[2]);

geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
const material = new THREE.LineBasicMaterial({ color: 0x3498db, linewidth: 2 });
const pentagram = new THREE.Line(geometry, material);
scene.add(pentagram);

    camera.position.z = 2;

    // Add lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0xffffff, 0.5);
    pointLight.position.set(2, 2, 2);
    scene.add(pointLight);

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        pentagram.rotation.x += 0.01;
        pentagram.rotation.y += 0.01;
        renderer.render(scene, camera);
    }
    animate();

    // Event listener for pentagram clicks
    renderer.domElement.addEventListener('click', (event) => {
        const rect = renderer.domElement.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        const y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera({ x, y }, camera);

        const intersects = raycaster.intersectObject(pentagram);

        if (intersects.length > 0) {
            fetch('/topics')
                .then(response => response.json())
                .then(topics => {
                    const clickedIndex = Math.floor(Math.random() * topics.length);
                    const topic = topics[clickedIndex];
                    console.log('Selected topic:', topic);

                    // Visual feedback
                    pentagram.material.color.setHex(0xff0000);
                    setTimeout(() => {
                        pentagram.material.color.setHex(0x3498db);
                    }, 500);

                    fetch(`/subtopics/${topic}`)
                        .then(response => response.json())
                        .then(subtopics => {
                            subtopicsDiv.innerHTML = `<h3>${topic} Subtopics:</h3>`;
                            subtopics.forEach(subtopic => {
                                const subtopicBtn = document.createElement('button');
                                subtopicBtn.textContent = subtopic;
                                subtopicBtn.addEventListener('click', () => {
                                    fetch(`/content/${topic}/${subtopic}`)
                                        .then(response => response.json())
                                        .then(data => {
                                            contentDiv.innerHTML = `<h2>${subtopic}</h2><p>${data.content}</p>`;
                                        })
                                        .catch(error => console.error('Error fetching content:', error));
                                });
                                subtopicsDiv.appendChild(subtopicBtn);
                            });
                        })
                        .catch(error => console.error('Error fetching subtopics:', error));
                })
                .catch(error => console.error('Error fetching topics:', error));
        }
    });
});

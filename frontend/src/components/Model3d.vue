<template>
    <div class="model3d-container">
        <div ref="container3D" class="model3d"></div>
    </div>
</template>

<script>
import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
import { OrbitControls } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js";
import { GLTFLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js";

export default {
    props: {
        modelPath: String, // Đường dẫn đến file .gltf của mô hình
    },
    mounted() {
        this.initScene();
    },
    methods: {
        initScene() {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(
                75,
                this.$refs.container3D.clientWidth / this.$refs.container3D.clientHeight,
                0.1,
                1000
            );

            const renderer = new THREE.WebGLRenderer({ alpha: true });
            renderer.setPixelRatio(window.devicePixelRatio);
            renderer.setSize(this.$refs.container3D.clientWidth, this.$refs.container3D.clientHeight);
            renderer.toneMapping = THREE.ACESFilmicToneMapping;
            renderer.toneMappingExposure = 1;
            this.$refs.container3D.appendChild(renderer.domElement);

            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.25;
            controls.screenSpacePanning = false;
            controls.minDistance = 2;
            controls.maxDistance = 10;
            controls.maxPolarAngle = Math.PI / 2;

            let object;

            const loader = new GLTFLoader();
            loader.load(
                this.modelPath,
                (gltf) => {
                    object = gltf.scene;
                    scene.add(object);
                    const box = new THREE.Box3().setFromObject(object);
                    const center = box.getCenter(new THREE.Vector3());
                    object.position.sub(center);
                },
                (xhr) => {
                    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
                },
                (error) => {
                    console.error(error);
                }
            );

            camera.position.z = 5;

            // Add lights to the scene, so we can actually see the 3D model
            const topLight = new THREE.DirectionalLight(0xffffff, 1); // (color, intensity)
            topLight.position.set(500, 500, 500); // top-left-ish
            topLight.castShadow = true;
            scene.add(topLight);

            const ambientLight = new THREE.AmbientLight(0x333333, 1);
            scene.add(ambientLight);

            // Render the scene
            const animate = () => {
                requestAnimationFrame(animate);

                // Tự động xoay mô hình theo phương thẳng đứng
                if (object) {
                    object.rotation.y += 0.01; // Thay đổi giá trị này để điều chỉnh tốc độ quay
                }

                controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true
                renderer.render(scene, camera);
            };

        

            window.addEventListener("resize", () => {
                camera.aspect = this.$refs.container3D.clientWidth / this.$refs.container3D.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(this.$refs.container3D.clientWidth, this.$refs.container3D.clientHeight);
            });
            animate();
        },
    },
};
</script>

<style scoped>
.model3d-container {
    width: 100%;
    height: 300px;
    /* Điều chỉnh chiều cao cho phù hợp */
    display: flex;
    justify-content: center;
    align-items: center;
}

.model3d {
    width: 80%;
    height: 100%;
    border: 3px solid black;
    box-sizing: border-box;
}
</style>
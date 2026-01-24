pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins descarga el código automáticamente, pero confirmamos qué rama es
                echo "📦 Trabajando en la rama: ${env.BRANCH_NAME}"
            }
        }

        stage('Lógica de Entorno') {
            steps {
                script {
                    // Usamos un bloque script para usar lógica de programación pura
                    if (env.BRANCH_NAME == 'main') {
                        echo "🚀 Iniciando despliegue para PRODUCCIÓN..."
                        echo "Configurando servicios en puerto 4006..."
                    } 
                    else if (env.BRANCH_NAME == 'develop') {
                        echo "🛠️ Iniciando despliegue para DESARROLLO..."
                        echo "Configurando servicios en puerto 4004..."
                    } 
                    else {
                        echo "🌿 Esta es una rama secundaria/feature: ${env.BRANCH_NAME}"
                    }
                }
            }
        }

        stage('Simulación de Build') {
            steps {
                echo "Compilando el código backend..."
                // Aquí irían tus comandos de docker o npm install
                sh 'echo "Simulando ejecución de comandos de terminal"'
            }
        }
    }

    post {
        success {
            echo "✅ ¡Pipeline finalizado con éxito en ${env.BRANCH_NAME}!"
        }
        failure {
            echo "❌ El pipeline falló. Revisa los logs."
        }
    }
}
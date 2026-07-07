#!/bin/bash
#? This script sets up a clean architecture project structure in Dart/Flutter.
# Define the base directory
BASE_DIR="lib"

# Create core directories and files
mkdir -p $BASE_DIR/core/errors
touch $BASE_DIR/core/errors/exceptions.dart
touch $BASE_DIR/core/errors/failures.dart

mkdir -p $BASE_DIR/core/network
touch $BASE_DIR/core/network/network_info.dart

mkdir -p $BASE_DIR/core/usecases
touch $BASE_DIR/core/usecases/usecase.dart

mkdir -p $BASE_DIR/core/util
touch $BASE_DIR/core/util/constants.dart
touch $BASE_DIR/core/util/input_converter.dart

mkdir -p $BASE_DIR/core/widgets
touch $BASE_DIR/core/widgets/loading_widget.dart
touch $BASE_DIR/core/widgets/message_display.dart

mkdir -p $BASE_DIR/core/themes
touch $BASE_DIR/core/themes/light_theme.dart
touch $BASE_DIR/core/themes/dark_theme.dart

# Define the features
FEATURES=(
  "authentication"
  "onboarding"
  "fleet_management"
  "driver_management"
)

# Create directories and files for each feature
for feature in "${FEATURES[@]}"
do
  # Data layer
  mkdir -p $BASE_DIR/features/$feature/data/datasources
  touch $BASE_DIR/features/$feature/data/datasources/${feature}_remote_data_source.dart
  
  mkdir -p $BASE_DIR/features/$feature/data/models
  touch $BASE_DIR/features/$feature/data/models/${feature}_model.dart
  
  mkdir -p $BASE_DIR/features/$feature/data/repositories
  touch $BASE_DIR/features/$feature/data/repositories/${feature}_repository_impl.dart
  
  # Domain layer
  mkdir -p $BASE_DIR/features/$feature/domain/entities
  touch $BASE_DIR/features/$feature/domain/entities/${feature}.dart
  
  mkdir -p $BASE_DIR/features/$feature/domain/repositories
  touch $BASE_DIR/features/$feature/domain/repositories/${feature}_repository.dart
  
  mkdir -p $BASE_DIR/features/$feature/domain/usecases
  touch $BASE_DIR/features/$feature/domain/usecases/${feature}_usecase.dart
  
  # Presentation layer
  mkdir -p $BASE_DIR/features/$feature/presentation/blocs
  touch $BASE_DIR/features/$feature/presentation/blocs/${feature}_bloc.dart
  
  mkdir -p $BASE_DIR/features/$feature/presentation/pages
  touch $BASE_DIR/features/$feature/presentation/pages/${feature}_page.dart
  
  mkdir -p $BASE_DIR/features/$feature/presentation/widgets
  touch $BASE_DIR/features/$feature/presentation/widgets/${feature}_widget.dart
done

# Create main.dart file
touch $BASE_DIR/main.dart

echo "Project structure created successfully."

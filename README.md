# Conversor de Sistemas Numéricos

Una aplicación de escritorio desarrollada en **C# con Windows Forms** que permite convertir números entre diferentes sistemas numéricos de forma rápida y sencilla.

## Características Principales

- **Interfaz gráfica moderna** con Windows Forms
- **Conversión instantánea** entre 4 sistemas numéricos
- **Validación robusta** de entrada de datos
- **Manejo de errores** con MessageBox informativos
- **Interfaz adaptativa** que muestra solo conversiones relevantes
- **Diseño profesional** con colores distintivos

## Sistemas Numéricos Soportados

| Sistema | Base | Ejemplo de Entrada | Ejemplo de Salida |
|---------|------|-------------------|-------------------|
| **Decimal** | Base 10 | `255` | `255` |
| **Binario** | Base 2 | `11111111` | `255` |
| **Octal** | Base 8 | `377` | `255` |
| **Hexadecimal** | Base 16 | `FF` | `255` |

## Instalación y Uso

### Requisitos del Sistema
- **Windows 7 o superior**
- **.NET Framework 4.7.2 o superior**
- **Visual Studio 2019/2022** (para desarrollo)

### Opción 1: Usar el Ejecutable (Recomendado)
1. Descarga `ConversorSistemasNumericos.exe` desde [Releases](../../releases)
2. Ejecuta el archivo directamente
3. ¡Listo para usar!

### Opción 2: Compilar desde Visual Studio

#### Paso a Paso en Visual Studio:
1. **Abre el proyecto** en Visual Studio
2. **Cambia a modo Release**:
   - En la barra superior: `Debug` → `Release`
3. **Compila el proyecto**:
   - `Build` → `Build Solution` (Ctrl + Shift + B)
4. **Encuentra tu ejecutable**:
   - Carpeta del proyecto → `bin/Release/ConversorSistemasNumericos.exe`

## Guía de Uso

### Conversión Paso a Paso

1. **Ingresa el número** en el TextBox principal
2. **Selecciona el sistema de origen** con los RadioButtons:
   - Decimal (0-9)
   - Binario (0-1)
   - Octal (0-7)  
   - Hexadecimal (0-9, A-F)
3. **Haz clic en "Convertir"**
4. **Ve los resultados** automáticamente en los campos correspondientes

### Ejemplos de Conversión

#### Ejemplo 1: Decimal → Otros Sistemas
```
Entrada: 255 (Decimal)
Resultados:
├── Binario: 11111111
├── Octal: 377
└── Hexadecimal: FF
```

#### Ejemplo 2: Binario → Otros Sistemas
```
Entrada: 1010 (Binario)
Resultados:
├── Decimal: 10
├── Octal: 12
└── Hexadecimal: A
```

#### Ejemplo 3: Hexadecimal → Otros Sistemas
```
Entrada: ABC (Hexadecimal)
Resultados:
├── Decimal: 2748
├── Binario: 101010111100
└── Octal: 5274
```

## Estructura del Proyecto

```
ConversorSistemasNumericos/
├── Forms/
│   ├── Form1.cs                 # Formulario principal
│   ├── Form1.Designer.cs        # Diseñador de formulario
│   └── Form1.resx              # Recursos del formulario
├── Classes/                     # (Opcional)
│   └── ConversorLogica.cs      # Lógica de conversión
├── Properties/
│   ├── AssemblyInfo.cs         # Información del ensamblado
│   └── Resources.resx          # Recursos del proyecto
├── Program.cs                   # Punto de entrada
├── App.config                  # Configuración de la aplicación
└── ConversorSistemasNumericos.csproj
```

## Componentes de la Interfaz

### Controles Principales
- **TextBox**: Campo de entrada del número
- **RadioButtons**: Selección del sistema origen
- **Labels**: Etiquetas descriptivas
- **TextBox (ReadOnly)**: Campos de resultado
- **Buttons**: Convertir, Limpiar, Salir
- **GroupBox/Panel**: Agrupación visual

### Eventos Implementados
```csharp
private void btnConvertir_Click(object sender, EventArgs e)
private void btnLimpiar_Click(object sender, EventArgs e)
private void rbDecimal_CheckedChanged(object sender, EventArgs e)
// ... otros eventos
```

## Validaciones y Manejo de Errores

### Validaciones C# Implementadas
```csharp
// Validación para números binarios
if (!System.Text.RegularExpressions.Regex.IsMatch(input, "^[01]+$"))
{
    MessageBox.Show("Número binario inválido", "Error", 
                   MessageBoxButtons.OK, MessageBoxIcon.Error);
    return;
}

// Validación para números octales
if (!System.Text.RegularExpressions.Regex.IsMatch(input, "^[0-7]+$"))
{
    MessageBox.Show("Número octal inválido", "Error", 
                   MessageBoxButtons.OK, MessageBoxIcon.Error);
    return;
}
```

### Excepciones Manejadas
- `FormatException`: Formato de número inválido
- `OverflowException`: Número demasiado grande
- `ArgumentException`: Argumentos inválidos

## Lógica de Conversión

### Métodos Principales
```csharp
public class ConversorNumericos
{
    public static int BinarioADecimal(string binario)
    public static int OctalADecimal(string octal)
    public static int HexADecimal(string hex)
    
    public static string DecimalABinario(int numero)
    public static string DecimalAOctal(int numero)
    public static string DecimalAHex(int numero)
}
```

### Ejemplo de Implementación
```csharp
private void ConvertirNumero()
{
    try
    {
        string input = txtEntrada.Text.Trim();
        int decimal_value = 0;
        
        // Convertir a decimal según el sistema origen
        switch (sistemaOrigen)
        {
            case "decimal":
                decimal_value = int.Parse(input);
                break;
            case "binario":
                decimal_value = Convert.ToInt32(input, 2);
                break;
            case "octal":
                decimal_value = Convert.ToInt32(input, 8);
                break;
            case "hexadecimal":
                decimal_value = Convert.ToInt32(input, 16);
                break;
        }
        
        // Mostrar resultados
        MostrarResultados(decimal_value);
    }
    catch (Exception ex)
    {
        MessageBox.Show($"Error: {ex.Message}", "Error de Conversión");
    }
}
```

## Cómo Generar el Ejecutable

### En Visual Studio:
1. **Cambiar a Release Mode**:
   ```
   Barra superior: Debug ▼ → Release
   ```

2. **Compilar el Proyecto**:
   ```
   Menu: Build → Build Solution
   Atajo: Ctrl + Shift + B
   ```

3. **Ubicar el Ejecutable**:
   ```
   Ruta: [Carpeta del Proyecto]\bin\Release\
   Archivo: ConversorSistemasNumericos.exe
   ```

### Archivos del Release:
```
Release/
├── ConversorSistemasNumericos.exe      # ← Ejecutable principal
├── ConversorSistemasNumericos.exe.config
├── ConversorSistemasNumericos.pdb      # (Opcional)
└── [DLLs adicionales si las hay]
```

## Casos de Prueba

| Entrada | Sistema Origen | Decimal | Binario | Octal | Hexadecimal |
|---------|----------------|---------|---------|--------|-------------|
| `10` | Decimal | - | `1010` | `12` | `A` |
| `1111` | Binario | `15` | - | `17` | `F` |
| `77` | Octal | `63` | `111111` | - | `3F` |
| `FF` | Hexadecimal | `255` | `11111111` | `377` | - |

## Solución de Problemas

### Error: "No se puede ejecutar en otro PC"
**Causa**: Falta .NET Framework
**Solución**: Instalar .NET Framework 4.7.2+

### Error: "Archivo no encontrado"
**Causa**: Faltan archivos de configuración
**Solución**: Copiar toda la carpeta `Release/`

### Error de Compilación
**Causa**: Referencias faltantes
**Solución**: 
1. `References` → `Add Reference`
2. Verificar .NET Framework version

##  Contribuciones

### Mejoras Sugeridas
- [ ] Soporte para números negativos
- [ ] Conversión con decimales
- [ ] Historial de conversiones
- [ ] Copiar al portapapeles
- [ ] Temas de colores (claro/oscuro)
- [ ] Conversión en tiempo real

### Cómo Contribuir
1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -m 'Agrega nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

##  Información Técnica

- **Lenguaje**: C#
- **Framework**: .NET Framework 4.7.2
- **UI**: Windows Forms
- **IDE**: Visual Studio 2019/2022
- **Target Platform**: Windows (Any CPU)

## Autor

- **Thaiz Avila** 

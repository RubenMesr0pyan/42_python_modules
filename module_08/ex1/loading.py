import sys
import importlib


def show_versions(modules):
    print("\nInstalled package versions:")
    for name, module in modules.items():
        version = getattr(module, "__version__", "unknown")
        print(f"- {name}: {version}")


print("LOADING STATUS: Loading programs...\n")

libs = ["numpy", "pandas", "matplotlib"]
modules = {}

print("Checking dependencies:")

for lib in libs:
    try:
        modules[lib] = importlib.import_module(lib)
        version = getattr(modules[lib], "__version__", "unknown")

        if lib == "numpy":
            print(f"[OK] {lib} ({version}) - Numerical computation ready")
        elif lib == "pandas":
            print(f"[OK] {lib} ({version}) - Data manipulation ready")
        elif lib == "matplotlib":
            print(f"[OK] {lib} ({version}) - Visualization ready")

    except ImportError:
        print(f"[MISSING] {lib}")
        print("\nInstall dependencies using pip:")
        print("pip install -r requirements.txt")
        print("\nOr using Poetry:")
        print("poetry install")
        sys.exit(1)

show_versions(modules)

print("\nDependency Management:")
print("- pip uses requirements.txt")
print("- Poetry uses pyproject.toml")

np = modules["numpy"]
pd = modules["pandas"]

plt = importlib.import_module("matplotlib.pyplot")

print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")

data = np.random.randint(0, 100, 1000)

df = pd.DataFrame(data, columns=["value"])

print("Generating visualization...")

plt.hist(df["value"], bins=20)
plt.title("Matrix Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.savefig("matrix_analysis.png")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")

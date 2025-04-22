import subprocess

with open("fold_pcc_log.csv", "w") as f:
    f.write("")  # Truncate the file

for fold in range(1, 11):
    print(f"\n🚀 Running fold {fold}...\n")
    result = subprocess.run(['python3', 'height.py', '--fold', str(fold)])

    if result.returncode != 0:
        print(f"❌ Fold {fold} failed with return code {result.returncode}")
        break

# After all folds, run the full summary block
print("\n✅ All folds completed. Generating saliency summary and top SNPs...\n")
subprocess.run(['python3', 'height.py', '--summary'])
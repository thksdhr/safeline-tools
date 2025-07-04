#!/bin/bash

#SCRIPT_NAME="get_ipgroup_list"
SCRIPT_NAME="main"
OUTPUT_DIR="dist"

# 清理旧文件
rm -rf build "$OUTPUT_DIR/$SCRIPT_NAME"

# 打包命令（可添加更多参数）
pyinstaller --onefile \
             --distpath="$OUTPUT_DIR" \
             --specpath="spec" \
             --workpath="build" \
             --noconfirm \
             --clean \
             "$SCRIPT_NAME.py"

# 检查是否成功
if [ -f "$OUTPUT_DIR/$SCRIPT_NAME" ]; then
    echo "✅ 打包成功！位于: $OUTPUT_DIR/$SCRIPT_NAME"
else
    echo "❌ 打包失败，请检查错误日志。"
    exit 1
fi
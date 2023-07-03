I would change this:

```suggestion
-      - uses: actions/checkout@v2
-#      - name: Read file content
-#        id: read-file
-#        run: |
+#      - uses: actions/checkout@v2
+      - name: Read file content
+        id: read-file
+        run: |
```
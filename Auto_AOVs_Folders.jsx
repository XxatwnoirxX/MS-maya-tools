{
    //==================================
    // ScriptName    : Auto AOVs Folder
    // Author        : Atsushi Hirata
    // Since         : 2023/07/12
    // Update        : None
    //==================================

    //自動的にAOVsに対応したフォルダーを生成するスクリプトです。

    function AutoAOVsFolder(thisObj)
    {
        var folderNames = ["material", "chara", "albedo", "beauty", "cryptmat", "cryptobj", "diffuse_direct", "shadowmatte", "specular_direct", "Z"
                            ,"bg", "albedo", "beauty", "cryptmat", "cryptobj", "diffuse_direct", "shadowmatte", "specular_direct", "Z"
                            ,"precomp"];
        var allFolders = folderNames.length -1;
        //var allFolders = 20;
        for (i = 1; i <= allFolders ; ++i){
            app.project.items.addFolder(folderNames[i]);
        }
        alert("フォルダを生成しました。");
    }
    AutoAOVsFolder(this);
}

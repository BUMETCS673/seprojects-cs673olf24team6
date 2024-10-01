module.exports = function override(config, env) {
    if (env === "test") {
        config.testEnvironment = "node";
        config.moduleFileExtensions.push("jsx", "ts", "tsx", "js", "json", "node");
        config.verbose = true;
    }
    return config;
};
java org.antlr.Tool -verbose -make -fo copypaster copypaster/Frontend.g
java org.antlr.Tool -verbose -make -fo copypaster copypaster/Backend.g
java org.antlr.Tool -verbose -make -fo autogenerated grammar/RecognizerFrontend.g
java org.antlr.Tool -verbose -make -fo autogenerated grammar/RecognizerBackend.g

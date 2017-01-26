package com.rxp170.rpmHelloWorld;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello Controller
 */
@RestController
public class HelloController {

    @RequestMapping("/")
    public String helloWorld(){
        return "Hello rpm!";
    }
}
